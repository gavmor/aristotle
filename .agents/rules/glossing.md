# Project Glossing Rule

When creating interlinear glosses in this vault, we integrate the global `/classical-gloss` skill with our local `/speak-greek` voice engine to automatically produce embedded audio.

**Workflow:**
1. Use the global `/classical-gloss` skill to segment the text and generate the `ngloss` block.
2. Use the local `/speak-greek` skill (in **Export Mode**) to generate an MP3 audio file of the Greek text. Save it to the vault's `assets/audio/` directory, naming it after the citation (e.g., `assets/audio/1145a25.mp3`).
3. Embed the audio file in the markdown directly above the `ngloss` block using standard Obsidian syntax (e.g., `![[1145a25.mp3]]`).
