import re

with open("concepts/self-love.md", "r") as f:
    text = f.read()

def repl(m):
    greek = m.group(1).split()
    translit = m.group(2).split()
    gloss = m.group(3).split()
    
    # get translation from the next line
    full_match = m.group(0)
    # this might be tricky, let's just do it manually with multi_replace_file_content 
    # since it's only 5 blocks and safer to ensure accuracy.
