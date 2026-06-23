# Plannotator for Typora

A dark [Typora](https://typora.io) theme ported from the **Plannotator** color scheme
used in [backnotprop/plannotator](https://github.com/backnotprop/plannotator) —
the local, browser-based review surface for AI coding agents.

The palette is taken from [`plannotator-zed.json`](https://github.com/backnotprop/plannotator)
(the Plannotator Zed editor theme): deep navy surfaces with a lavender primary
accent (`#9a9dff`) and a warm orange secondary accent (`#f47700`).

![palette](https://img.shields.io/badge/background-%23070b14-070b14) ![palette](https://img.shields.io/badge/accent-%239a9dff-9a9dff) ![palette](https://img.shields.io/badge/orange-%23f47700-f47700) ![palette](https://img.shields.io/badge/green-%233fc168-3fc168)

## Install

1. Download [`plannotator.css`](./plannotator.css).
2. In Typora: **Preferences → Appearance → Open Theme Folder**.
3. Drop `plannotator.css` into that folder.
4. Restart Typora and pick **Plannotator** from **Themes**.

> Requires Typora ≥ 0.9.12 (Windows) / 0.9.9.5.1 (macOS).

## Features

- **Faithful syntax highlighting** — CodeMirror tokens in both fenced code
  blocks (`.cm-s-inner`) **and** source code mode (`.cm-s-typora-default`) are
  mapped from the Zed `syntax` palette.
- **Readable document hierarchy** — h1 uses cyan, h2 uses the Plannotator
  lavender title color, and smaller headings stay closer to body text.
- Full coverage of blockquotes, tables, task lists, YAML front matter, math,
  diagrams, TOC, focus mode, callouts, sidebar/file-list, search highlights,
  and print styles.
- **Inter** for body, **JetBrains Mono** for code (falls back to system fonts).

## Palette

| Token | Hex | Used for |
|---|---|---|
| `background` | `#070b14` | page / editor background |
| `surface` | `#151b24` | sidebar, code, blockquote, table stripes |
| `elevated` | `#222935` | table headers, menus, popovers |
| `text` | `#dadee5` | body text |
| `accent` | `#9a9dff` | links, h2, selected UI |
| `orange` | `#f47700` | `strong`, list markers, numbers/constants |
| `cyan` | `#00c0cf` | h1, inline code, constructors, labels |
| `teal` | `#00ab93` | types, operators |
| `green` | `#3fc168` | strings |
| `amber` | `#d9a514` | warnings |
| `red` | `#f14d4c` | errors |
| `magenta` | `#d568ea` | keywords, tags |
| `gold` | `#ffca00` | functions |
| `salmon` | `#ffa359` | variables |
| `indigo` | `#9d6afb` | properties |
| `mint` | `#61d5c0` | attributes |

## Repository contents

| File | Description |
|---|---|
| [`plannotator.css`](./plannotator.css) | The Typora theme. |
| [`plannotator-zed.json`](./plannotator-zed.json) | Original Zed editor theme — the source-of-truth palette this Typora theme is ported from. |
| [`plannotator-ui.css`](./plannotator-ui.css) | Original Plannotator *product UI* design-token theme (verbatim, oklch/shadcn-style) — kept for reference. Not a Typora theme. |

## Credits

- Color scheme © the [backnotprop/plannotator](https://github.com/backnotprop/plannotator)
  project (MIT / Apache-2.0 dual licensed).
- This Typora port is independently authored.

## License

MIT
