import sys
from cltk import NLP

def main():
    try:
        # Initialize NLP for Ancient Greek
        print("Initializing CLTK with Stanza...")
        cltk_nlp = NLP(language_code="grc", suppress_banner=True)
        
        # Test text
        text = "ἄνδρα μοι ἔννεπε, μοῦσα, πολύτροπον, ὃς μάλα πολλὰ"
        print("Processing...")
        doc = cltk_nlp.analyze(text=text)
        
        lemmas = [word.lemma for word in doc.words]
        print("Lemmas:", lemmas)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
