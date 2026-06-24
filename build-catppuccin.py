#!/usr/bin/env python3
"""
Generate Catppuccin Typora themes (one .css per flavor).

All four flavors share the exact same rule set; only the 26-color palette
(plus a handful of derived alpha tokens) changes. This script keeps them in
sync: edit the TEMPLATE / FUNCTIONAL / BODY blocks once and regenerate.

Palette: official catppuccin/palette v1.8.0 (https://github.com/catppuccin/palette)
Usage:   python3 build-catppuccin.py
"""

PALETTE_VERSION = "1.8.0"

# ---- official hex values (catppuccin/palette) -----------------------------
FLAVORS = {
    "latte": {
        "label": "Latte", "emoji": "🌻", "dark": False,
        "rosewater": "#dc8a78", "flamingo": "#dd7878", "pink": "#ea76cb",
        "mauve": "#8839ef", "red": "#d20f39", "maroon": "#e64553",
        "peach": "#fe640b", "yellow": "#df8e1d", "green": "#40a02b",
        "teal": "#179299", "sky": "#04a5e5", "sapphire": "#209fb5",
        "blue": "#1e66f5", "lavender": "#7287fd", "text": "#4c4f69",
        "subtext1": "#5c5f77", "subtext0": "#6c6f85", "overlay2": "#7c7f93",
        "overlay1": "#8c8fa1", "overlay0": "#9ca0b0", "surface2": "#acb0be",
        "surface1": "#bcc0cc", "surface0": "#ccd0da", "base": "#eff1f5",
        "mantle": "#e6e9ef", "crust": "#dce0e8",
    },
    "frappe": {
        "label": "Frappé", "emoji": "🪴", "dark": True,
        "rosewater": "#f2d5cf", "flamingo": "#eebebe", "pink": "#f4b8e4",
        "mauve": "#ca9ee6", "red": "#e78284", "maroon": "#ea999c",
        "peach": "#ef9f76", "yellow": "#e5c890", "green": "#a6d189",
        "teal": "#81c8be", "sky": "#99d1db", "sapphire": "#85c1dc",
        "blue": "#8caaee", "lavender": "#babbf1", "text": "#c6d0f5",
        "subtext1": "#b5bfe2", "subtext0": "#a5adce", "overlay2": "#949cbb",
        "overlay1": "#838ba7", "overlay0": "#737994", "surface2": "#626880",
        "surface1": "#51576d", "surface0": "#414559", "base": "#303446",
        "mantle": "#292c3c", "crust": "#232634",
    },
    "macchiato": {
        "label": "Macchiato", "emoji": "🌺", "dark": True,
        "rosewater": "#f4dbd6", "flamingo": "#f0c6c6", "pink": "#f5bde6",
        "mauve": "#c6a0f6", "red": "#ed8796", "maroon": "#ee99a0",
        "peach": "#f5a97f", "yellow": "#eed49f", "green": "#a6da95",
        "teal": "#8bd5ca", "sky": "#91d7e3", "sapphire": "#7dc4e4",
        "blue": "#8aadf4", "lavender": "#b7bdf8", "text": "#cad3f5",
        "subtext1": "#b8c0e0", "subtext0": "#a5adcb", "overlay2": "#939ab7",
        "overlay1": "#8087a2", "overlay0": "#6e738d", "surface2": "#5b6078",
        "surface1": "#494d64", "surface0": "#363a4f", "base": "#24273a",
        "mantle": "#1e2030", "crust": "#181926",
    },
    "mocha": {
        "label": "Mocha", "emoji": "🌿", "dark": True,
        "rosewater": "#f5e0dc", "flamingo": "#f2cdcd", "pink": "#f5c2e7",
        "mauve": "#cba6f7", "red": "#f38ba8", "maroon": "#eba0ac",
        "peach": "#fab387", "yellow": "#f9e2af", "green": "#a6e3a1",
        "teal": "#94e2d5", "sky": "#89dceb", "sapphire": "#74c7ec",
        "blue": "#89b4fa", "lavender": "#b4befe", "text": "#cdd6f4",
        "subtext1": "#bac2de", "subtext0": "#a6adc8", "overlay2": "#9399b2",
        "overlay1": "#7f849c", "overlay0": "#6c7086", "surface2": "#585b70",
        "surface1": "#45475a", "surface0": "#313244", "base": "#1e1e2e",
        "mantle": "#181825", "crust": "#11111b",
    },
}

PALETTE_ORDER = [
    "rosewater", "flamingo", "pink", "mauve", "red", "maroon", "peach",
    "yellow", "green", "teal", "sky", "sapphire", "blue", "lavender",
    "text", "subtext1", "subtext0", "overlay2", "overlay1", "overlay0",
    "surface2", "surface1", "surface0", "base", "mantle", "crust",
]


def rgba(hexc, a):
    h = hexc.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r}, {g}, {b}, {a})"


def root_block(flavor):
    c = FLAVORS[flavor]
    lines = ["  /* ---- raw Catppuccin palette (official hex) ---- */"]
    for name in PALETTE_ORDER:
        lines.append(f"  --{name}: {c[name]};")

    alpha = f"""
  /* ---- derived alpha tokens (flavor-specific) ---- */
  --select-bg:        {rgba(c['mauve'], 0.25)};
  --select-bg-strong: {rgba(c['mauve'], 0.40)};
  --search-active-bg: {rgba(c['peach'], 0.45)};
  --mark-bg:          {rgba(c['yellow'], 0.28)};
  --activeline-bg:    {rgba(c['surface0'], 0.50)};
  --drop-target-bg:   {rgba(c['blue'], 0.18)};
  --modal-backdrop:   {rgba(c['crust'], 0.72)};"""

    return "\n".join(lines) + "\n" + alpha + "\n" + FUNCTIONAL


# Functional aliases — IDENTICAL across flavors (reference palette vars above).
FUNCTIONAL = """
  /* ---- functional aliases (Typora chrome + theme tokens) ---- */
  --bg-color:                 var(--base);
  --side-bar-bg-color:        var(--mantle);
  --surface:                  var(--mantle);
  --elevated:                 var(--surface0);
  --hover:                    var(--surface0);
  --active:                   var(--surface1);

  --border:                   var(--surface1);
  --border-soft:              var(--surface0);
  --window-border:            1px solid var(--surface1);

  --text-color:               var(--text);
  --text-muted:               var(--subtext0);
  --text-dim:                 var(--overlay0);
  --md-char-color:            var(--overlay1);
  --meta-content-color:       var(--subtext0);
  --control-text-color:       var(--subtext1);

  --accent:                   var(--mauve);
  --primary-color:            var(--mauve);
  --primary-btn-border-color: var(--mauve);

  --code-bg:                  var(--mantle);
  --inline-code-bg:           var(--surface0);

  --select-text-bg-color:     var(--select-bg);
  --item-hover-bg-color:      var(--surface0);
  --item-hover-text-color:    var(--text);
  --active-file-bg-color:     var(--surface0);
  --active-file-text-color:   var(--text);
  --active-file-border-color: var(--mauve);
  --rawblock-edit-panel-bd:   var(--mantle);
"""


def header(flavor):
    c = FLAVORS[flavor]
    return f"""/*
 * Catppuccin {c['label']} {c['emoji']}  —  Typora theme
 * ----------------------------------------------------------------------------
 * The "{c['label']}" flavor of Catppuccin (https://catppuccin.com), the
 * community-driven soothing pastel theme. Official palette v{PALETTE_VERSION}.
 *
 * Syntax mapping follows the Catppuccin Style Guide:
 *   keywords=mauve · strings=green · functions=blue · numbers/constants=peach
 *   types=yellow · operators=sky · comments=overlay · accent=mauve
 *
 * Install:
 *   1. Typora -> Preferences -> Appearance -> "Open Theme Folder"
 *   2. Copy this file ({_filename(flavor)}) into that folder.
 *   3. Restart Typora and pick "Catppuccin {c['label']}" from Themes.
 */
"""


def _filename(flavor):
    return f"catppuccin-{flavor}.css"


# ---------------------------------------------------------------------------
# The full Typora rule set. Uses functional aliases + raw palette names so it
# is identical for every flavor. Edit here once.
# ---------------------------------------------------------------------------
BODY = r"""
/* ============================================================
 * Base
 * ========================================================== */
html {
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html,
body {
  margin: auto;
  background: var(--bg-color);
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
  fill: currentColor;
}

body {
  color: var(--text-color);
  font-family: "Inter", "PingFang SC", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.7;
}

content { background: var(--bg-color); }

#write {
  max-width: 860px;
  margin: 0 auto;
  padding: 42px 32px 96px;
  color: var(--text-color);
}

@media only screen and (min-width: 1400px) { #write { max-width: 980px; } }
@media only screen and (min-width: 1800px) { #write { max-width: 1080px; } }
@media only screen and (max-width: 640px) {
  html { font-size: 15px; }
  #write { padding: 26px 18px 64px; }
}

#write > p:first-child,
#write > ul:first-child,
#write > ol:first-child,
#write > pre:first-child,
#write > blockquote:first-child,
#write > div:first-child,
#write > table:first-child,
#write > h1:first-child,
#write > h2:first-child { margin-top: 0; }

/* ============================================================
 * Headings — Catppuccin accent sweep (cool -> green)
 * ========================================================== */
#write h1,
#write h2,
#write h3,
#write h4,
#write h5,
#write h6 {
  margin: 1.6em 0 0.6em;
  padding: 0;
  font-weight: 700;
  line-height: 1.25;
  letter-spacing: -0.01em;
  color: var(--mauve);
  clear: both;
  word-wrap: break-word;
}

#write h1 {
  margin-top: 0.4em;
  font-size: 2.15em;
  letter-spacing: -0.02em;
  padding-bottom: 0.34em;
  border-bottom: 1px solid var(--border);
  color: var(--mauve);
}
#write h2 {
  font-size: 1.6em;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--border-soft);
  color: var(--blue);
}
#write h3 { font-size: 1.3em;  color: var(--sapphire); }
#write h4 { font-size: 1.12em; color: var(--teal); }
#write h5 { font-size: 1em;    color: var(--green); }
#write h6 { font-size: 0.9em;  color: var(--subtext0); text-transform: none; }

.md-heading:hover .md-heading-fold-button { color: var(--mauve); }

/* ============================================================
 * Inline elements
 * ========================================================== */
p,
.mathjax-block { margin-top: 0; margin-bottom: 1rem; }

a {
  color: var(--blue);
  text-decoration: none;
  transition: color 0.15s ease;
}
a:hover { color: var(--sky); text-decoration: underline; }

strong, b { color: var(--peach); font-weight: 700; }
em, i, dfn, cite { color: var(--mauve); font-style: italic; }

mark {
  border-radius: 3px;
  padding: 0.05em 0.3em;
  background: var(--mark-bg);
  color: var(--text-color);
}
del { color: var(--text-dim); }

sup.md-footnote {
  background: var(--surface0);
  color: var(--mauve);
  font-size: 0.8em;
}
sup.md-footnote:hover { color: var(--blue); }

kbd {
  display: inline-block;
  padding: 1px 6px;
  font-size: 0.82em;
  font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
  color: var(--text-color);
  background: var(--surface0);
  border: 1px solid var(--border);
  border-radius: 4px;
  box-shadow: 0 1px 0 var(--border-soft);
}

/* ============================================================
 * Lists
 * ========================================================== */
ul, ol { padding-left: 1.7em; margin-bottom: 1rem; }
li { margin: 0.18em 0; }
li::marker { color: var(--peach); }
ul ul, ol ol, ul ol, ol ul { margin: 0.2em 0; }

.task-list,
.contains-task-list { padding-left: 0; list-style: none; }
.md-task-list-item,
.task-list-item {
  padding-left: 1.6rem;
  list-style: none !important;
  list-style-type: none !important;
}
.md-task-list-item::marker,
.task-list-item::marker {
  content: "";
  color: transparent;
  font-size: 0;
}
.md-task-list-item > input[type="checkbox"],
.task-list-item > input[type="checkbox"] {
  -webkit-appearance: none !important;
  appearance: none !important;
  opacity: 1 !important;
  display: inline-grid;
  place-content: center;
  box-sizing: border-box;
  width: 1.05rem !important;
  height: 1.05rem !important;
  min-width: 1.05rem;
  margin: 0.35em 0 0 -1.45rem !important;
  padding: 0;
  vertical-align: middle;
  border: 1.5px solid var(--border);
  border-radius: 4px;
  background: var(--bg-color);
  cursor: pointer;
}
.md-task-list-item > input[type="checkbox"]:checked,
.md-task-list-item > input[type="checkbox"][checked],
.task-list-item > input[type="checkbox"]:checked,
.task-list-item > input[type="checkbox"][checked] {
  border-color: var(--green);
  background: var(--green);
}
.md-task-list-item > input[type="checkbox"]:checked::after,
.md-task-list-item > input[type="checkbox"][checked]::after,
.task-list-item > input[type="checkbox"]:checked::after,
.task-list-item > input[type="checkbox"][checked]::after {
  content: "\2713";
  font-size: 0.72rem;
  font-weight: 700;
  line-height: 1;
  color: var(--base);
}

/* ============================================================
 * Blockquote & hr
 * ========================================================== */
blockquote {
  margin: 1.2em 0;
  padding: 0.5em 1.1em;
  border-left: 4px solid var(--mauve);
  border-radius: 0 6px 6px 0;
  background: var(--surface);
  color: var(--text-color);
}
blockquote blockquote {
  border-left-color: var(--blue);
  background: var(--surface0);
}
blockquote blockquote blockquote { border-left-color: var(--teal); }

hr {
  height: 1px;
  margin: 2.2em 0;
  border: 0;
  background: linear-gradient(90deg, transparent, var(--border) 20%, var(--border) 80%, transparent);
}

/* ============================================================
 * Code — fonts, inline code, fenced blocks
 * ========================================================== */
code, pre, .md-fences, #typora-source, .md-meta-block {
  font-family: "JetBrains Mono", "SF Mono", "Cascadia Code", "Fira Code",
    Menlo, Consolas, "PingFang SC", monospace;
}

code, tt {
  font-size: 0.88em;
  padding: 0.1em 0.38em;
  border-radius: 4px;
  border: 1px solid var(--border-soft);
  background: var(--inline-code-bg);
  color: var(--green);
}

.md-fences {
  margin: 1.2em 0 1.5em;
  padding: 14px 16px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--code-bg);
  color: var(--text-color);
  font-size: 0.88em;
  line-height: 1.55;
}
.md-fences .code-tooltip {
  background: var(--elevated);
  border: 1px solid var(--border);
}
.enable-diagrams pre.md-fences[lang="sequence"] .code-tooltip,
.enable-diagrams pre.md-fences[lang="flow"] .code-tooltip,
.enable-diagrams pre.md-fences[lang="mermaid"] .code-tooltip { bottom: -2.2em; }

/* ============================================================
 * CodeMirror syntax — follows the Catppuccin Style Guide
 *   .cm-s-inner          => fenced code blocks
 *   .cm-s-typora-default => source code mode
 * ========================================================== */
.cm-s-inner, .cm-s-typora-default {
  background: var(--code-bg);
  color: var(--text-color);
}
.cm-s-inner .CodeMirror-cursor,
.cm-s-typora-default .CodeMirror-cursor { border-left: 2px solid var(--rosewater); }

.cm-s-inner .CodeMirror-selected,
.cm-s-inner .CodeMirror-line::selection,
.cm-s-inner .CodeMirror-line > span::selection,
.cm-s-inner .CodeMirror-line > span > span::selection,
.cm-s-typora-default .CodeMirror-selected { background: var(--select-bg); }

.cm-s-inner .CodeMirror-activeline-background,
.cm-s-typora-default .CodeMirror-activeline-background { background: var(--activeline-bg); }

.cm-s-inner .CodeMirror-gutters,
.cm-s-typora-default .CodeMirror-gutters {
  background: var(--code-bg);
  border-right: 1px solid var(--border-soft);
}
.cm-s-inner .CodeMirror-linenumber,
.cm-s-typora-default .CodeMirror-linenumber { color: var(--overlay0); }

.cm-s-inner .cm-keyword,      .cm-s-typora-default .cm-keyword      { color: var(--mauve); }
.cm-s-inner .cm-atom,         .cm-s-typora-default .cm-atom         { color: var(--peach); }
.cm-s-inner .cm-number,       .cm-s-typora-default .cm-number       { color: var(--peach); }
.cm-s-inner .cm-def,          .cm-s-typora-default .cm-def          { color: var(--blue); }
.cm-s-inner .cm-builtin,      .cm-s-typora-default .cm-builtin      { color: var(--red); }
.cm-s-inner .cm-qualifier,    .cm-s-typora-default .cm-qualifier    { color: var(--blue); }
.cm-s-inner .cm-variable,     .cm-s-typora-default .cm-variable     { color: var(--text-color); }
.cm-s-inner .cm-variable-2,   .cm-s-typora-default .cm-variable-2   { color: var(--lavender); }
.cm-s-inner .cm-variable-3,   .cm-s-typora-default .cm-variable-3   { color: var(--yellow); }
.cm-s-inner .cm-type,         .cm-s-typora-default .cm-type         { color: var(--yellow); }
.cm-s-inner .cm-property,     .cm-s-typora-default .cm-property     { color: var(--blue); }
.cm-s-inner .cm-operator,     .cm-s-typora-default .cm-operator     { color: var(--sky); }
.cm-s-inner .cm-comment,      .cm-s-typora-default .cm-comment      { color: var(--overlay0); font-style: italic; }
.cm-s-inner .cm-string,       .cm-s-typora-default .cm-string       { color: var(--green); }
.cm-s-inner .cm-string-2,     .cm-s-typora-default .cm-string-2     { color: var(--teal); }
.cm-s-inner .cm-meta,         .cm-s-typora-default .cm-meta         { color: var(--pink); }
.cm-s-inner .cm-header,       .cm-s-typora-default .cm-header       { color: var(--mauve); font-weight: 700; }
.cm-s-inner .cm-link,         .cm-s-typora-default .cm-link         { color: var(--blue); }
.cm-s-inner .cm-strong,       .cm-s-typora-default .cm-strong       { color: var(--peach); font-weight: 700; }
.cm-s-inner .cm-em,           .cm-s-typora-default .cm-em           { color: var(--mauve); font-style: italic; }
.cm-s-inner .cm-tag,          .cm-s-typora-default .cm-tag          { color: var(--blue); }
.cm-s-inner .cm-attribute,    .cm-s-typora-default .cm-attribute    { color: var(--yellow); }
.cm-s-inner .cm-bracket,      .cm-s-typora-default .cm-bracket      { color: var(--overlay2); }
.cm-s-inner .cm-punctuation,  .cm-s-typora-default .cm-punctuation  { color: var(--overlay2); }
.cm-s-inner .cm-error,        .cm-s-typora-default .cm-error        { color: var(--red); }
.cm-s-inner .CodeMirror-matchingbracket,
.cm-s-typora-default .CodeMirror-matchingbracket {
  color: var(--mauve) !important;
  text-decoration: underline;
}

/* ============================================================
 * YAML front matter
 * ========================================================== */
#write pre.md-meta-block {
  min-height: 30px;
  margin: 0 0 2em;
  padding: 12px 1em;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--surface);
  color: var(--text-muted);
  font-size: 0.85em;
  line-height: 1.7em;
  white-space: pre;
}

/* ============================================================
 * Tables
 * ========================================================== */
table {
  width: 100%;
  margin: 1.2em 0 1.6em;
  border-collapse: collapse;
  border-spacing: 0;
  overflow: hidden;
  border-radius: 8px;
}
table th, table td {
  padding: 9px 14px;
  border: 1px solid var(--border);
  line-height: 1.5;
  vertical-align: top;
}
table th {
  background: var(--elevated);
  color: var(--mauve);
  font-weight: 700;
  text-align: left;
}
table td { background: var(--bg-color); }
table tbody tr:nth-child(odd) td { background: var(--surface); }
table tbody tr:hover td { background: var(--surface0); }
.ty-table-edit { background: var(--elevated); border-top: 1px solid var(--border); }

/* ============================================================
 * Images & math
 * ========================================================== */
.md-image > .md-meta {
  color: var(--text-muted);
  background: var(--surface);
  border-radius: 4px;
}
.md-image > img { border-radius: 6px; }

.md-inline-math script, .md-inline-math svg { color: var(--blue); }
#math-inline-preview .md-arrow:after { background: var(--elevated); }
.md-mathjax-midline { background: var(--surface); }
.md-inline-math .md-math-block { color: var(--text-color); }

#write .md-focus .md-diagram-panel {
  border: 1px solid var(--border);
  border-radius: 8px;
  background: var(--code-bg);
}
.md-diagram-panel-error { color: var(--red); }

/* ============================================================
 * Table of contents
 * ========================================================== */
.md-toc { margin-top: 2.2em; }
.md-toc-content { padding-bottom: 16px; color: var(--text-muted); }
.md-toc-item { color: var(--text-color); }
.md-toc-item:hover { color: var(--mauve); }
#write div.md-toc-tooltip { background: var(--bg-color); }
#toc-dropmenu {
  background: var(--elevated);
  border: 1px solid var(--border);
}
#toc-dropmenu .divider { background-color: var(--border); }

.outline-expander:before { color: inherit; top: auto; }
.outline-item:hover { background: var(--surface0); color: var(--text-color); }
.outline-label:hover { text-decoration: none; }

/* ============================================================
 * Search highlights & selection
 * ========================================================== */
::selection { background: var(--select-bg); }
::-moz-selection { background: var(--select-bg); }
*.in-text-selection { background: var(--select-bg); }

.md-search-hit {
  background: var(--select-bg-strong);
  border-radius: 2px;
}
.md-search-hit.md-search-select { background: var(--search-active-bg); }

/* ============================================================
 * Sidebar / file list / outline
 * ========================================================== */
#typora-sidebar {
  color: var(--text-color);
  background: var(--side-bar-bg-color);
  border-right: 1px solid var(--border-soft);
}
#typora-sidebar:hover div.sidebar-content-content::-webkit-scrollbar-thumb:horizontal {
  background: var(--border);
}
.html-for-mac #typora-sidebar { box-shadow: 0 6px 18px rgba(0, 0, 0, 0.28); }
.sidebar-tabs { border-bottom: 1px solid var(--border-soft); }
.sidebar-tab { color: var(--text-muted); }
.sidebar-tab.active { color: var(--mauve); border-bottom-color: var(--mauve); }

.file-list-item,
.file-library-node { color: var(--text-color); }
.file-list-item.active,
.file-library-node.active > .file-node-content { color: var(--active-file-text-color); }
.file-list-item.active,
.file-library-node.active > .file-node-background { background: var(--active-file-bg-color) !important; }
.file-list-item:hover,
.file-node-content:hover { background: var(--item-hover-bg-color); }
.file-list-item-summary,
.file-list-item-time,
.file-list-item-parent-loc,
.file-node-title { color: var(--text-muted); }
#sidebar-files-menu {
  border: 1px solid var(--border);
  background: var(--elevated);
  box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.4);
}
.outline-title-wrapper .btn,
.sidebar-footer-item { color: var(--text-muted); }
.sidebar-footer-item:hover { background: var(--surface0); color: var(--text-color); }

/* ============================================================
 * UI chrome — header / footer / menus / dialogs
 * ========================================================== */
header,
footer,
.context-menu,
.megamenu-content,
.modal-content,
#typora-quick-open,
.auto-suggest-container,
.popover {
  font-family: "Inter", "PingFang SC", -apple-system, BlinkMacSystemFont, sans-serif;
}

.megamenu-opened header,
.megamenu-menu-panel { background: var(--side-bar-bg-color); }
header { background: var(--bg-color); border-bottom: 1px solid var(--border-soft); }
footer.ty-footer { border-color: var(--border-soft); background: var(--bg-color); color: var(--text-muted); }

.context-menu,
#spell-check-panel,
#footer-word-count-info { background-color: var(--elevated); color: var(--text-color); }
.context-menu.dropdown-menu .divider,
.dropdown-menu .divider { background-color: var(--border); }

.modal-content { background: var(--side-bar-bg-color); border: 1px solid var(--border); }
.modal-content input { background: var(--bg-color); color: var(--text-color); border: 1px solid var(--border); }
.modal-backdrop { background-color: var(--modal-backdrop); }
.modal-title { font-size: 1.3em; }
.popover { background: var(--elevated); border: 1px solid var(--border); }
.popover.bottom > .arrow:after { border-bottom-color: var(--elevated); }
.popover.top > .arrow:after { border-top-color: var(--elevated); }

#md-searchpanel { border-bottom: 1px solid var(--border-soft); background: var(--bg-color); }
#md-searchpanel input { color: var(--text-color); }

.btn,
.btn .btn-default { background: transparent; color: var(--text-color); border: 1px solid var(--border); }
.btn:hover, .btn-default:hover { background: var(--surface0); color: var(--text-color); }
.btn-primary { color: var(--crust); background: var(--mauve); border-color: var(--mauve); }

#typora-quick-open, .auto-suggest-container { background: var(--elevated); border: 1px solid var(--border); }
.typora-quick-open-item.active,
.typora-quick-open-item:hover { background: var(--mauve); color: var(--crust); }

.ty-preferences .nav-group-item.active,
.export-item.active { background: var(--surface0); }
.ty-preferences input[type="search"] { background: var(--bg-color); border-color: var(--border); color: var(--text-color); }
.ty-preferences select { border: 1px solid var(--border); }

#ty-tooltip { background: var(--elevated); color: var(--text-color); border: 1px solid var(--border); }
div.code-tooltip, .md-hover-tip .md-arrow:after { background: var(--elevated); }

/* ============================================================
 * Focus / typewriter mode
 * ========================================================== */
.on-focus-mode .md-end-block:not(.md-focus):not(.md-focus-container) * {
  color: var(--text-dim) !important;
}
.on-focus-mode .md-end-block:not(.md-focus) img,
.on-focus-mode .md-task-list-item:not(.md-focus-container) > input,
.on-focus-mode .task-list-item:not(.md-focus-container) > input {
  opacity: 0.4 !important;
}
.on-focus-mode .md-fences.md-focus .CodeMirror-code > *:not(.CodeMirror-activeline) *,
.on-focus-mode .CodeMirror.cm-s-inner:not(.CodeMirror-focused) * {
  color: var(--text-dim) !important;
}
.on-focus-mode #typora-source .CodeMirror-code > *:not(.CodeMirror-activeline) * {
  color: var(--text-dim) !important;
}
.on-focus-mode .md-focus,
.on-focus-mode .md-focus-container { color: var(--text-color); }

/* ============================================================
 * GitHub-style alert / callout blocks
 * ========================================================== */
.md-alert-text-note      { color: var(--blue); }
.md-alert-text-tip       { color: var(--green); }
.md-alert-text-important { color: var(--mauve); }
.md-alert-text-warning   { color: var(--yellow); }
.md-alert-text-caution   { color: var(--red); }
.md-alert-text-abstract  { color: var(--teal); }
.md-alert-text-info      { color: var(--sapphire); }
.md-alert-text-todo      { color: var(--blue); }
.md-alert-text-success   { color: var(--green); }
.md-alert-text-question  { color: var(--teal); }
.md-alert-text-failure   { color: var(--red); }
.md-alert-text-danger    { color: var(--red); }
.md-alert-text-bug       { color: var(--red); }
.md-alert-text-example   { color: var(--peach); }
.md-alert-text-quote     { color: var(--subtext0); }

/* ============================================================
 * Scrollbars
 * ========================================================== */
::-webkit-scrollbar { width: 9px; height: 9px; }
::-webkit-scrollbar-track { background: var(--bg-color); }
::-webkit-scrollbar-thumb {
  border-radius: 5px;
  background: var(--surface2);
  border: 2px solid var(--bg-color);
}
::-webkit-scrollbar-thumb:hover { background: var(--overlay0); }
::-webkit-scrollbar-thumb:active { background: var(--overlay1); }

/* ============================================================
 * Print — always export on white for legibility
 * ========================================================== */
@media print {
  html { font-size: 12pt; background: #fff; }
  body { background: #fff; color: #4c4f69; }
  #write { max-width: none; padding: 0; }

  #write h1, #write h2 { color: #8839ef; border-color: #ccd0da; }
  #write h3 { color: #209fb5; }
  #write h4 { color: #179299; }
  #write h5 { color: #40a02b; }
  #write h6 { color: #6c6f85; }

  a { color: #1e66f5; }
  strong, b { color: #fe640b; }
  code, .md-fences, blockquote, #write pre.md-meta-block,
  table th, table td {
    background: #eff1f5 !important;
    border-color: #ccd0da !important;
    color: #4c4f69 !important;
  }
  code, tt { color: #40a02b !important; }
  #typora-sidebar, header, footer, #md-searchpanel { display: none !important; }
}
"""


def build():
    for flavor, c in FLAVORS.items():
        css = header(flavor) + "\n:root {\n" + root_block(flavor) + "}\n" + BODY
        fname = _filename(flavor)
        with open(fname, "w") as f:
            f.write(css)
        print(f"wrote {fname}  ({len(css):,} bytes)  [Catppuccin {c['label']}]")


if __name__ == "__main__":
    build()
