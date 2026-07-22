import sys
import re
import stanza

def main():
    print("Downloading Stanza Greek models...")
    stanza.download('grc')
    
    print("Initializing Stanza pipeline (tokenize, lemma)...")
    # We only need tokenize and lemma to save time
    nlp = stanza.Pipeline('grc', processors='tokenize,pos,lemma', use_gpu=False)
    
    print("Reading text...")
    with open('/home/user/Documents/aristotle/references/nicomachean-ethics-greek.xml', 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Cleaning XML tags...")
    text = re.sub(r'<[^>]+>', ' ', text)
    
    print("Lemmatizing (this may take a minute)...")
    # Processing in a single batch might run out of memory, let's process in chunks if needed, 
    # but 120k words should be okay for 8GB RAM.
    doc = nlp(text)
    
    megas_count = 0
    metrios_count = 0
    
    for sentence in doc.sentences:
        for word in sentence.words:
            if word.lemma:
                # Stanza might output lemmas with accents
                lemma = word.lemma.lower()
                if lemma == 'μέγας' or lemma == 'μεγας':
                    megas_count += 1
                elif lemma == 'μέτριος' or lemma == 'μετριος':
                    metrios_count += 1
                    
    print(f"Total 'μέγας' lemma count: {megas_count}")
    print(f"Total 'μέτριος' lemma count: {metrios_count}")

if __name__ == "__main__":
    main()
