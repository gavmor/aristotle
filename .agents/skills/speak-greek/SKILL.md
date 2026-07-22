---
name: speak-greek
description: Speak or pronounce Ancient Greek text out loud. Use this skill whenever the user uses the `/speak-greek` slash command, asks to hear a Greek passage, or asks how to pronounce a Greek word.
---
# Speak Greek

This skill allows you to synthesize audio for Ancient Greek text using Microsoft's `edge-tts` and play it back directly to the user.

## Instructions

When the user asks you to speak or pronounce Ancient Greek text (e.g. `/speak-greek μῆνιν ἄειδε θεὰ`), you must use the `run_command` tool to execute the following pipeline. 

Because `edge-tts` modern Greek voices will fail on classical polytonic diacritics, the pipeline first strips the diacritics using Python's `unicodedata`, then pipes the output through `ffplay`.

**Voice Engine Modes:**
This skill acts as the centralized Voice Engine for classical Greek, owning the `edge-tts` voice settings, playback rate, and diacritic-stripping logic. It can be run in two modes:

1. **Interactive Mode** (Default): When a user asks to hear text via the slash command, generate the mp3 to `/tmp/` and play it immediately using `ffplay`.
2. **Export Mode**: When invoked by another skill (like `/classical-gloss`) or when the user explicitly asks to save the audio, generate the mp3 to the requested permanent location (e.g. `assets/audio/`) and DO NOT play it.

**Bash Command Generation Pipeline:**
```bash
TEXT="[INSERT_GREEK_TEXT_HERE]" && OUTFILE="[INSERT_OUTPUT_PATH].mp3" && edge-tts --voice el-GR-NestorasNeural --rate=-60% --text "$(echo "$TEXT" | python3 -c "import sys, unicodedata as u; print(''.join(c for c in u.normalize('NFD', sys.stdin.read()) if u.category(c) != 'Mn').strip())")" --write-media "$OUTFILE"
```

### Steps:
1. Extract the Ancient Greek text the user wants to hear. If the user provided a mix of English and Greek, extract ONLY the Greek text to avoid the Greek voice trying to read English words.
2. Determine the mode:
   - If **Interactive**, set `[INSERT_OUTPUT_PATH]` to `/tmp/[CITATION_OR_SNIPPET]` and append `&& ffplay -nodisp -autoexit -loglevel quiet "$OUTFILE"` to the command.
   - If **Export**, set `[INSERT_OUTPUT_PATH]` to the requested path (like `assets/audio/[CITATION]`) and execute the generation pipeline as-is.
3. Replace `[INSERT_GREEK_TEXT_HERE]` with the target text, ensuring proper escaping.
4. Run the command using the `run_command` tool.
5. Notify the user: 
   - If Interactive, say the audio is playing and provide a clickable markdown file link to the `/tmp/` file as backup.
   - If Export, say the audio has been saved to the specified location.
