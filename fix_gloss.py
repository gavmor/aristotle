import re

with open("concepts/self-love.md", "r", encoding="utf-8") as f:
    text = f.read()

# The regex will find the blockquote and the following code block, and the next paragraph starting with *
pattern = r"> (.*?)\n\n```\n(.*?)\n(.*?)\n(.*?)\n```\n\n\*(.*?)\* (.*)"

def repl(m):
    greek_sent = m.group(1).strip()
    g_words = m.group(2).split()
    t_words = m.group(3).split()
    e_words = m.group(4).split()
    trans_sent = m.group(5).strip()
    rest_of_para = m.group(6).strip()
    
    out = f"```ngloss\n\\ex {greek_sent}\n\\gl "
    lines = []
    for g, t, e in zip(g_words, t_words, e_words):
        lines.append(f"{g} [{t}] [{e}]")
    
    out += lines[0] + "\n"
    for line in lines[1:]:
        out += "    " + line + "\n"
    out += f"\\ft {trans_sent}\n```\n\n{rest_of_para}"
    return out

new_text = re.sub(pattern, repl, text)

with open("concepts/self-love.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Done")
