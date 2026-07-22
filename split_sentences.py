import json

with open('praxis_sentences.json', 'r', encoding='utf-8') as f:
    sentences = json.load(f)

chunk_size = 10
for i in range(0, len(sentences), chunk_size):
    chunk = sentences[i:i+chunk_size]
    with open(f'praxis_chunk_{i//chunk_size}.json', 'w', encoding='utf-8') as f:
        json.dump(chunk, f, ensure_ascii=False, indent=2)

print(f"Created {len(sentences)//chunk_size + 1} chunks.")
