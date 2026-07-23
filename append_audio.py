import re

with open("concepts/self-love.md", "r", encoding="utf-8") as f:
    text = f.read()

# The audio files in order
files = ["1168b19.mp3", "1168b30.mp3", "1169a3.mp3", "1169a32.mp3", "1169a11.mp3"]

# We can replace '```\n\n' with '```\n![[audio.mp3]]\n\n' but we need to do it only for ngloss blocks
# The regex can match ```ngloss ... \ft ... \n```\n
# Let's use a function and a counter

counter = 0
def repl(m):
    global counter
    out = m.group(0) + f"![[{files[counter]}]]\n"
    counter += 1
    return out

# Match from ```ngloss down to the closing ```\n
new_text = re.sub(r'```ngloss.*?\\ft.*?\n```\n', repl, text, flags=re.DOTALL)

with open("concepts/self-love.md", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Appended audio embeds. Counter:", counter)
