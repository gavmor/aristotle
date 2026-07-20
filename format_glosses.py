import re

with open('concepts/courage.md', 'r') as f:
    content = f.read()

# Pattern to find the gloss sections
# We look for:
# > Greek text
# \n```\n
# word1 word2 ...
# translit1 translit2 ...
# gloss1 gloss2 ...
# \n```\n
# \n*Translation.* Prose...

pattern = re.compile(r'> (.*?)\n\n```\n(.*?)\n(.*?)\n(.*?)\n```\n\n\*(.*?)\* (.*)', re.MULTILINE)

def replacer(match):
    greek_quote = match.group(1).strip()
    words = match.group(2).split()
    translits = match.group(3).split()
    glosses = match.group(4).split()
    translation = match.group(5).strip()
    rest_of_prose = match.group(6).strip()
    
    # Construct the ngloss block
    ngloss = f"```ngloss\n\\ex {greek_quote}\n\\gl "
    
    lines = []
    for w, t, g in zip(words, translits, glosses):
        lines.append(f"{w} [{t}] [{g}]")
    
    ngloss += lines[0] + "\n"
    for line in lines[1:]:
        ngloss += "    " + line + "\n"
        
    ngloss += f"\\ft {translation}\n```\n\n{rest_of_prose}"
    return ngloss

new_content = pattern.sub(replacer, content)

with open('concepts/courage.md', 'w') as f:
    f.write(new_content)

print("Updated concepts/courage.md")
