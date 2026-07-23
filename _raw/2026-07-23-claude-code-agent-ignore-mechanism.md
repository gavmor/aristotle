---
title: Claude Code has no .claudeignore/.agentignore — use permissions.deny in settings.json
tags: [claude-code, obsidian, wiki-maintenance, config]
project: aristotle
sources:
  - "aristotle session (2026-07-23)"
created: 2026-07-23T21:46:41Z
updated: 2026-07-23T21:46:41Z
lifecycle: raw
lifecycle_changed: 2026-07-23
provenance:
  extracted: 0.8
  inferred: 0.2
base_confidence: 0.8
summary: Claude Code has no native ignore-file mechanism; agent-visibility exclusions must be expressed as tool-scoped permissions.deny path globs in .claude/settings.json.
---

## Finding

Unlike Cursor (`.cursorignore`), Gemini CLI (`.geminiignore`), or the proposed cross-tool `.agentignore` standard, **Claude Code has no dedicated ignore-file format**. The equivalent mechanism is `permissions.deny` entries in `.claude/settings.json`, using tool-scoped path-glob rules of the form `Tool(./path/**)`, e.g.:

```json
{
  "permissions": {
    "deny": [
      "Read(./docs/**)",
      "Edit(./docs/**)",
      "Write(./docs/**)"
    ]
  }
}
```

Each rule is scoped per-tool (`Read`, `Edit`, `Write`, `Bash`, etc.) rather than being a single blanket path exclusion the way `.gitignore`-style files work — so fully "ignoring" a path means adding one deny entry per tool you want blocked (Read to keep it out of context, Edit/Write to prevent modification). ^[extracted]

Project-scoped settings (`.claude/settings.json`, git-committed) is the right file for repo-structural ignore policy that should apply to any contributor working in the repo; `.claude/settings.local.json` (gitignored) is for personal-only overrides. ^[inferred]

## Project-specific state (aristotle vault)

In this vault, `docs/` (a generated site export mirroring the wiki — `index.html`, `order.txt`, `references/`, `synthesis/`, `entities/`, `concepts/`) and the two large raw source dumps listed in `.gitignore` (`Nicomachean Ethics - Aristotle.epub`, `Nicomachean Ethics - Aristotle.txt`) were placed off-limits to the agent via `.claude/settings.json`.

After the initial deny list was written, it was edited externally (by the user or a linter) to **remove the `Read` deny on the `.txt` file** while keeping `Read` denied on the `.epub` and `Edit`/`Write` denied on both. Effective final state: the `.txt` dump remains readable (likely still needed as a source for some workflow) but not editable; the `.epub` is fully off-limits; `docs/` is fully off-limits (no read/edit/write). ^[extracted]

## Related

- [[concepts/contemplative-life]] — unrelated content page edited earlier in the same session, included here only for vault connectivity
