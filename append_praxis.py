import os

files = [f"praxis_out_{i}.md" for i in range(12)]
content = "\n## Exhaustive Praxis Citations\n\n"

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as inf:
            content += inf.read() + "\n"

with open('concepts/praxis.md', 'a', encoding='utf-8') as outf:
    outf.write(content)

print(f"Appended {len(content)} bytes to concepts/praxis.md")

for f in files:
    if os.path.exists(f):
        os.remove(f)

for f in os.listdir('.'):
    if f.startswith('praxis_chunk_'):
        os.remove(f)
if os.path.exists('praxis_sentences.json'):
    os.remove('praxis_sentences.json')
