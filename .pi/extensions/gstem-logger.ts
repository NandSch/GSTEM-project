/**
 * G-Stem live chatlogger + GEBRUIKER-hub
 *
 * Projectextension voor ~/Documents/GSTEM-Project.
 * - Maakt GEBRUIKER/ aan met chat.md, index.md, onderwerpen.md en data/.
 * - Schrijft elk gebruikersbericht (verbatim) en elk AI-antwoord (volledig, zonder
 *   denkproces) live naar GEBRUIKER/chat.md.
 * - Archiveert chat.md automatisch naar GEBRUIKER/archief/<JJJJ-MM-DD_UUMM_slug>/
 *   zodra een nieuwe sessie start, plus een meta.md met topics.
 * - Commando's: /archiveer, /logboek, /onderwerp <naam>.
 *
 * Tool-calls en systeem-/toolresultaatberichten worden NIET gelogd.
 */

import {
	appendFileSync,
	existsSync,
	mkdirSync,
	readFileSync,
	renameSync,
	writeFileSync,
} from "node:fs";
import { dirname, join, resolve } from "node:path";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const CONFIG_DIR = ".pi";

function findProjectRoot(cwd: string): string {
	let dir = resolve(cwd);
	for (;;) {
		if (existsSync(join(dir, CONFIG_DIR, "extensions")) || existsSync(join(dir, CONFIG_DIR, "skills"))) {
			return dir;
		}
		const parent = dirname(dir);
		if (parent === dir) return resolve(cwd);
		dir = parent;
	}
}

const pad = (n: number) => String(n).padStart(2, "0");
const stamp = (d = new Date()) =>
	`${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}_${pad(d.getHours())}${pad(d.getMinutes())}`;
const clock = (d = new Date()) => `${pad(d.getHours())}:${pad(d.getMinutes())}`;
const iso = (d = new Date()) => d.toISOString();

function slugify(input: string): string {
	return (
		input
			.normalize("NFKD")
			.replace(/[\u0300-\u036f]/g, "")
			.toLowerCase()
			.replace(/[^a-z0-9]+/g, "-")
			.replace(/^-+|-+$/g, "")
			.slice(0, 48) || "sessie"
	);
}

function userText(content: unknown): { text: string; images: number } {
	if (typeof content === "string") return { text: content, images: 0 };
	let text = "";
	let images = 0;
	for (const part of (content as any[]) ?? []) {
		if (!part) continue;
		if (part.type === "text") text += (text ? "\n" : "") + part.text;
		else if (part.type === "image") images++;
	}
	return { text, images };
}

function assistantText(content: unknown): string {
	let text = "";
	for (const part of (content as any[]) ?? []) {
		if (part?.type === "text") text += (text ? "\n" : "") + part.text;
	}
	return text.trim();
}

function quote(text: string): string {
	return text
		.split("\n")
		.map((line) => "> " + line)
		.join("\n");
}

interface SessionState {
	sessionId?: string;
	startedAt?: number;
	slug?: string | null;
	messageCount?: number;
	topics?: { slug: string; title: string }[];
}

export default function gstemLogger(pi: ExtensionAPI) {
	let root = resolve(process.cwd());
	let gebrDir = join(root, "GEBRUIKER");
	let chatFile = join(gebrDir, "chat.md");
	let stateFile = join(gebrDir, ".sessie.json");
	let state: SessionState = {};
	let slugSet = false;

	function paths() {
		gebrDir = join(root, "GEBRUIKER");
		chatFile = join(gebrDir, "chat.md");
		stateFile = join(gebrDir, ".sessie.json");
	}

	function ensureDirs() {
		for (const sub of ["", "archief", "data"]) {
			mkdirSync(join(gebrDir, sub), { recursive: true });
		}
	}

	function loadState() {
		try {
			state = JSON.parse(readFileSync(stateFile, "utf8")) as SessionState;
		} catch {
			state = {};
		}
	}

	function saveState() {
		try {
			writeFileSync(stateFile, JSON.stringify(state, null, 2), "utf8");
		} catch {
			/* stil falen mag */
		}
	}

	function hasRealContent(): boolean {
		if (!existsSync(chatFile)) return false;
		try {
			return /^## /m.test(readFileSync(chatFile, "utf8"));
		} catch {
			return false;
		}
	}

	function freshChat(sessionId: string) {
		const now = new Date();
		const body = [
			"---",
			"tags: [gstem, chatlog]",
			`sessie: "${sessionId}"`,
			`gestart: ${iso(now)}`,
			"---",
			"",
			"# Live chat — huidige sessie",
			"",
			`> [!abstract] Sessie \`${sessionId}\` · gestart ${stamp(now)}`,
			"> Dit bestand wordt automatisch live bijgewerkt door de G-Stem logger.",
			"> Oudere sessies: [[archief/README|archief]]. Onderwerpen: [[onderwerpen]]. Data: [[index]].",
			"",
		].join("\n");
		writeFileSync(chatFile, body, "utf8");
	}

	function archivePrevious() {
		if (!hasRealContent()) return;
		ensureDirs();
		const prev = state;
		const when = prev.startedAt ? stamp(new Date(prev.startedAt)) : stamp();
		const slug = prev.slug || "sessie";
		let dir = join(gebrDir, "archief", `${when}_${slug}`);
		let n = 2;
		while (existsSync(dir)) {
			dir = join(gebrDir, "archief", `${when}_${slug}-${n}`);
			n++;
		}
		mkdirSync(dir, { recursive: true });
		renameSync(chatFile, join(dir, "chat.md"));

		// Snapshot van het onderwerpenregister, indien aanwezig.
		const onderwerpen = join(gebrDir, "onderwerpen.md");
		if (existsSync(onderwerpen)) {
			try {
				writeFileSync(join(dir, "onderwerpen.md"), readFileSync(onderwerpen, "utf8"), "utf8");
			} catch {
				/* negeren */
			}
		}

		const topics = Array.isArray(prev.topics) ? prev.topics : [];
		const meta = [
			"---",
			"tags: [gstem, chatarchief]",
			`sessie: "${prev.sessionId ?? "onbekend"}"`,
			`gestart: ${prev.startedAt ? iso(new Date(prev.startedAt)) : "onbekend"}`,
			`gearchiveerd: ${iso(new Date())}`,
			`berichten: ${prev.messageCount ?? "?"}`,
			"---",
			"",
			`# Sessie ${when}_${slug}`,
			"",
			"## Onderwerpen",
			topics.length
				? topics.map((t) => `- [[${t.slug}|${t.title}]]`).join("\n")
				: "- (geen via /onderwerp geregistreerd; zie `onderwerpen.md`)",
			"",
			"Volledig transcript: `chat.md` in deze map.",
			"",
		].join("\n");
		writeFileSync(join(dir, "meta.md"), meta, "utf8");

		const readme = join(gebrDir, "archief", "README.md");
		if (!existsSync(readme)) {
			writeFileSync(
				readme,
				"# Archief van sessies\n\nElke afgeronde sessie staat in een eigen map met `chat.md` en `meta.md`.\n\n",
				"utf8",
			);
		}
	}

	pi.on("session_start", async (_event, ctx) => {
		root = findProjectRoot(ctx.cwd);
		paths();
		ensureDirs();
		loadState();
		const sessionId = ctx.sessionManager.getSessionId();
		if (state.sessionId !== sessionId) {
			archivePrevious();
			freshChat(sessionId);
			state = { sessionId, startedAt: Date.now(), slug: null, messageCount: 0, topics: [] };
			slugSet = false;
			saveState();
		} else {
			if (!existsSync(chatFile)) freshChat(sessionId);
			slugSet = Boolean(state.slug);
		}
	});

	pi.on("message_end", async (event, ctx) => {
		const msg = event.message as any;
		if (!msg) return;

		// Alleen berichten van de hoofd-sessie loggen; subagents e.d. overslaan.
		if (state.sessionId && ctx.sessionManager.getSessionId() !== state.sessionId) return;

		if (msg.role === "user") {
			const { text, images } = userText(msg.content);
			if (!text.trim() && !images) return;
			if (!slugSet && text.trim()) {
				state.slug = slugify(text);
				slugSet = true;
			}
			state.messageCount = (state.messageCount ?? 0) + 1;
			saveState();
			const body = text.trim() || "*(afbeelding)*";
			const imageNote = images ? `\n>\n> _${images} afbeelding(en) bijgevoegd._` : "";
			appendFileSync(
				chatFile,
				`\n## Gebruiker · ${clock()}\n\n> [!quote] Verbatim\n${quote(body)}${imageNote}\n`,
				"utf8",
			);
			return;
		}

		if (msg.role === "assistant") {
			const text = assistantText(msg.content);
			if (!text) return;
			state.messageCount = (state.messageCount ?? 0) + 1;
			saveState();
			appendFileSync(chatFile, `\n## AI · ${clock()}\n\n${text}\n\n---\n`, "utf8");
		}
	});

	pi.on("session_shutdown", async (event, ctx) => {
		// Bij volledig afsluiten deze sessie alsnog archiveren.
		// Bij reload/new/resume/fork volgt een nieuwe session_start die archiveert.
		if (event.reason !== "quit") return;
		if (state.sessionId && ctx.sessionManager.getSessionId() !== state.sessionId) return;
		if (hasRealContent()) archivePrevious();
		// Voorkom dubbel archiveren bij een volgende start.
		state = { ...state, sessionId: undefined, messageCount: 0 };
		saveState();
	});

	pi.registerCommand("archiveer", {
		description: "Archiveer de huidige chat.md en begin een verse sessie-log",
		handler: async (_args, ctx) => {
			if (!hasRealContent()) {
				ctx.ui.notify("Er is nog niets om te archiveren.", "info");
				return;
			}
			archivePrevious();
			const sessionId = ctx.sessionManager.getSessionId();
			freshChat(sessionId);
			state = {
				sessionId,
				startedAt: Date.now(),
				slug: null,
				messageCount: 0,
				topics: state.topics ?? [],
			};
			slugSet = false;
			saveState();
			ctx.ui.notify("Sessie gearchiveerd in GEBRUIKER/archief/.", "info");
		},
	});

	pi.registerCommand("logboek", {
		description: "Toon het huidige GEBRUIKER/chat.md",
		handler: async (_args, ctx) => {
			if (!existsSync(chatFile)) {
				ctx.ui.notify("Nog geen chat.md.", "info");
				return;
			}
			await ctx.ui.editor("GEBRUIKER/chat.md", readFileSync(chatFile, "utf8"));
		},
	});

	pi.registerCommand("onderwerp", {
		description: "Maak/koppel een onderwerp (usage: /onderwerp <naam>)",
		handler: async (args, ctx) => {
			const name = args.trim();
			if (!name) {
				ctx.ui.notify("Gebruik: /onderwerp <naam>", "warning");
				return;
			}
			const slug = slugify(name);
			ensureDirs();
			const file = join(gebrDir, "data", `${slug}.md`);
			if (!existsSync(file)) {
				writeFileSync(
					file,
					[
						"---",
						"tags: [gstem, onderwerp]",
						`onderwerp: "${name}"`,
						`aangemaakt: ${iso(new Date())}`,
						"---",
						"",
						`# ${name}`,
						"",
					].join("\n"),
					"utf8",
				);
			}
			const idx = join(gebrDir, "onderwerpen.md");
			const current = existsSync(idx) ? readFileSync(idx, "utf8") : "# Onderwerpen\n\n";
			if (!current.includes(`[[${slug}`)) {
				appendFileSync(idx, `- [[${slug}|${name}]]\n`, "utf8");
			}
			state.topics = state.topics ?? [];
			if (!state.topics.some((t) => t.slug === slug)) {
				state.topics.push({ slug, title: name });
				saveState();
			}
			ctx.ui.notify(`Onderwerp '${name}' gekoppeld (data/${slug}.md).`, "info");
		},
	});
}
