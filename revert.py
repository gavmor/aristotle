with open('concepts/praxis.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
for line in lines:
    if line.strip() == "## Exhaustive Praxis Citations":
        break
    out_lines.append(line)

with open('concepts/praxis.md', 'w', encoding='utf-8') as f:
    f.writelines(out_lines)
