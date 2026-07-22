import re
import json

with open('/home/user/Documents/aristotle/references/nicomachean-ethics-greek.xml', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to find all sentences containing the target forms.
# First, let's remove some formatting but keep milestones to track citations.
# A sentence can be defined as ending with . ; · !
# But TEI XML has tags scattered inside sentences.
# Let's parse with basic string matching or regular expressions.

target_forms = {'πρᾶξις', 'πρᾶξίς', 'πρᾶξιν', 'πρᾶξίν', 'πράξεως', 'πράξει', 'πράξεις', 'πράξεων', 'πράξεσι', 'πράξεσιν'}

# We'll split the text into tokens. To keep track of milestones, we can keep them as special tokens.
tokens = re.split(r'(<[^>]+>|[\s\.\;·\,]+)', text)
tokens = [t for t in tokens if t]

current_page = ""
current_line = ""
current_book = ""

sentences = []
current_sentence = []
current_sentence_citation = ""

for token in tokens:
    if token.startswith('<'):
        if 'milestone unit="page"' in token:
            m = re.search(r'n="([^"]+)"', token)
            if m:
                current_page = m.group(1)
        elif 'milestone unit="line"' in token:
            m = re.search(r'n="([^"]+)"', token)
            if m:
                current_line = m.group(1)
        elif 'div type="book"' in token:
             m = re.search(r'n="([^"]+)"', token)
             if m:
                 current_book = m.group(1)
        continue
    
    # Not a tag
    # If the sentence is just starting, record the citation
    if not current_sentence:
        current_sentence_citation = f"Bk. {current_book} (Bekker {current_page}{current_line})"
        
    current_sentence.append(token)
    
    if any(p in token for p in ['.', ';', '·']):
        # End of sentence
        # Check if any target form is in this sentence
        # We need to strip punctuation to check
        has_target = False
        for w in current_sentence:
            w_clean = re.sub(r'[^\w]', '', w.lower())
            if w_clean in target_forms:
                has_target = True
                break
        
        if has_target:
            # Reconstruct sentence text
            sentence_text = "".join(current_sentence).strip()
            # Clean up extra spaces
            sentence_text = re.sub(r'\s+', ' ', sentence_text)
            sentences.append({
                "citation": current_sentence_citation,
                "greek": sentence_text
            })
            
        current_sentence = []

# Clean up any remaining
if current_sentence:
    has_target = False
    for w in current_sentence:
        w_clean = re.sub(r'[^\w]', '', w.lower())
        if w_clean in target_forms:
            has_target = True
            break
    if has_target:
        sentence_text = "".join(current_sentence).strip()
        sentence_text = re.sub(r'\s+', ' ', sentence_text)
        sentences.append({
            "citation": current_sentence_citation,
            "greek": sentence_text
        })

print(f"Found {len(sentences)} sentences.")
with open('praxis_sentences.json', 'w', encoding='utf-8') as f:
    json.dump(sentences, f, ensure_ascii=False, indent=2)

