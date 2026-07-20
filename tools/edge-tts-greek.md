---
title: "Ancient Greek Text-to-Speech (Edge TTS)"
category: tools
tags: [greek, audio, tts, edge-tts, python, scripting]
aliases: [edge-tts greek, greek tts]
created: 2026-07-20T00:00:00Z
updated: 2026-07-20T00:00:00Z
summary: A bash snippet using edge-tts and Python's unicodedata to strip polytonic diacritics for raw PCM playback of Ancient Greek text.
lifecycle: draft
tier: supporting
relationships: []
---

# Ancient Greek Text-to-Speech (Edge TTS)

To synthesize audio for Ancient Greek text using `edge-tts`, the classical polytonic diacritics must first be stripped (normalized) to avoid parsing errors from the modern Greek voice models.

This can be done using Python's `unicodedata` library in a bash function, which normalizes the text to NFD (decomposition) and strips out the `Mn` (Nonspacing_Mark) categories. The clean text is then piped to `edge-tts` (using the modern Greek voice `el-GR-NestorasNeural`) to generate raw PCM audio, which is played directly via `aplay`.

## Bash Function

This function can be added to your dotfiles (e.g., via `chezmoi`) to make it a permanent, reusable command:

```bash
speak_grc() {
    # 1. Strip classical polytonic diacritics to avoid edge-tts parsing errors
    local clean_text
    clean_text=$(echo "$1" | python3 -c "import sys, unicodedata as u; print(''.join(c for c in u.normalize('NFD', sys.stdin.read()) if u.category(c) != 'Mn').strip())")
    
    # 2. Request raw PCM from Microsoft and stream it directly into aplay
    edge-tts \
        --voice el-GR-NestorasNeural \
        --text "$clean_text" \
        --audio-format raw-24khz-16bit-mono-pcm \
        --write-media /dev/stdout | \
    aplay -q -t raw -f S16_LE -r 24000 -c 1
}
```

### Usage Example

```bash
speak_grc "μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος"
```

## One-Liner Version

If you need to execute it directly without a function wrapper:

```bash
TEXT="μῆνιν ἄειδε θεὰ" && edge-tts --voice el-GR-NestorasNeural --text "$(echo "$TEXT" | python3 -c "import sys, unicodedata as u; print(''.join(c for c in u.normalize('NFD', sys.stdin.read()) if u.category(c) != 'Mn').strip())")" --audio-format raw-24khz-16bit-mono-pcm --write-media /dev/stdout | aplay -q -t raw -f S16_LE -r 24000 -c 1
```
