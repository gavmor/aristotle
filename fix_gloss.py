import sys
import re

if len(sys.argv) < 2:
    print("No files provided")
    sys.exit(1)

for file_path in sys.argv[1:]:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'>\s*(.*?)\n\n```\n(.*?)\n(.*?)\n(.*?)\n```\n\n\*"([^"]+)"\*', re.MULTILINE | re.DOTALL)

    def replacer(match):
        original_quote = match.group(1).strip()
        greek_row = match.group(2).split()
        translit_row = match.group(3).split()
        gloss_row = match.group(4).split()
        translation = match.group(5).strip()
        
        out = [f"```ngloss\n\\ex {original_quote}"]
        
        if len(greek_row) == len(translit_row) == len(gloss_row):
            for i in range(len(greek_row)):
                prefix = "\\gl " if i == 0 else "    "
                out.append(f"{prefix}{greek_row[i]} [{translit_row[i]}] [{gloss_row[i]}]")
        else:
            print(f"Warning length mismatch: {len(greek_row)} {len(translit_row)} {len(gloss_row)}")
            for i in range(min(len(greek_row), len(translit_row), len(gloss_row))):
                prefix = "\\gl " if i == 0 else "    "
                out.append(f"{prefix}{greek_row[i]} [{translit_row[i]}] [{gloss_row[i]}]")
                
        out.append(f"\\ft {translation}\n```\n")
        return "\n".join(out)

    new_content = pattern.sub(replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Done processing {file_path}")
