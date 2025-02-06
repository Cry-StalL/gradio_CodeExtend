import type { Extension } from "@codemirror/state";
import { StreamLanguage } from "@codemirror/language";
import { sql } from "@codemirror/legacy-modes/mode/sql";
import { _ } from "svelte-i18n";

const possible_langs = [
	"python",
	"c",
	"cpp",
	"markdown",
	"json",
	"html",
	"css",
	"javascript",
	"jinja2",
	"typescript",
	"yaml",
	"dockerfile",
	"shell",
	"r",
	"sql",
	"go"
];

const sql_dialects = [
	"standardSQL",
	"msSQL",
	"mySQL",
	"mariaDB",
	"sqlite",
	"cassandra",
	"plSQL",
	"hive",
	"pgSQL",
	"gql",
	"gpSQL",
	"sparkSQL",
	"esper"
] as const;

const lang_map: Record<string, (() => Promise<Extension>) | undefined> = {
	python: () => import("@codemirror/lang-python").then((m) => m.python()),
	c: () =>
		import("@codemirror/legacy-modes/mode/clike").then((m) =>
			StreamLanguage.define(m.c)
		),
	cpp: () =>
		import("@codemirror/legacy-modes/mode/clike").then((m) =>
			StreamLanguage.define(m.cpp)
		),
	markdown: async () => {
		const [md, frontmatter] = await Promise.all([
			import("@codemirror/lang-markdown"),
			import("./frontmatter")
		]);
		return md.markdown({ extensions: [frontmatter.frontmatter] });
	},
	json: () => import("@codemirror/lang-json").then((m) => m.json()),
	html: () => import("@codemirror/lang-html").then((m) => m.html()),
	css: () => import("@codemirror/lang-css").then((m) => m.css()),
	javascript: () =>
		import("@codemirror/lang-javascript").then((m) => m.javascript()),
	jinja2: () =>
		import("@codemirror/legacy-modes/mode/jinja2").then((m) =>
			StreamLanguage.define(m.jinja2)
		),
	typescript: () =>
		import("@codemirror/lang-javascript").then((m) =>
			m.javascript({ typescript: true })
		),
	yaml: () =>
		import("@codemirror/legacy-modes/mode/yaml").then((m) =>
			StreamLanguage.define(m.yaml)
		),
	dockerfile: () =>
		import("@codemirror/legacy-modes/mode/dockerfile").then((m) =>
			StreamLanguage.define(m.dockerFile)
		),
	shell: () =>
		import("@codemirror/legacy-modes/mode/shell").then((m) =>
			StreamLanguage.define(m.shell)
		),
	r: () =>
		import("@codemirror/legacy-modes/mode/r").then((m) =>
			StreamLanguage.define(m.r)
		),
	sql: () =>
		import("@codemirror/legacy-modes/mode/sql").then((m) =>
			StreamLanguage.define(m.standardSQL)
		),
	...Object.fromEntries(
		sql_dialects.map((dialect) => [
			"sql-" + dialect,
			() =>
				import("@codemirror/legacy-modes/mode/sql").then((m) =>
					StreamLanguage.define(m[dialect])
				)
		])
	),

	go: () =>
		import("@codemirror/lang-go").then((m) => m.go()),
	java: () =>
		import("@codemirror/lang-java").then((m) => m.java()),
	liquid: () =>
		import("@codemirror/lang-liquid").then((m) => m.liquid()),
	php: () =>
		import("@codemirror/lang-php").then((m) => m.php()),
	rust: () =>
		import("@codemirror/lang-rust").then((m) => m.rust()),
	scss: () =>
		import("@codemirror/lang-sass").then((m) => m.sass()), // 该库支持sass/SCSS，其中有一个indented参数(When enabled, support classical indentation-based syntax)，默认为false，即SCSS syntax
	vue: () =>
		import("@codemirror/lang-vue").then((m) => m.vue()),
	xml: () =>
		import("@codemirror/lang-xml").then((m) => m.xml()),

} as const;

const alias_map: Record<string, string> = {
	py: "python",
	md: "markdown",
	js: "javascript",
	ts: "typescript",
	sh: "shell"
};

export async function getLanguageExtension(
	lang: string
): Promise<Extension | undefined> {
	const _lang = lang_map[lang] || lang_map[alias_map[lang]] || undefined;
	if (_lang) {
		return _lang();
	}
	return undefined;
}
