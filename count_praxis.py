import re

with open('/home/user/Documents/aristotle/references/nicomachean-ethics-greek.xml', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove XML tags
text = re.sub(r'<[^>]+>', ' ', text)

# Find all words
words = re.findall(r'[\p{L}\p{M}]+', text)
# In python re, to use unicode categories we need the 'regex' module.
# Since we might only have standard 're', let's use a simpler approach:
