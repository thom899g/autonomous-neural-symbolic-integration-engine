import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, text):
        try:
            doc = self.nlp(text)
            return {
                "ents": [(ent.text, ent.label_) for ent in doc.ents],
                "tokens": [token.text for token in doc]
            }
        except Exception as e:
            raise ValueError(f"NLP processing failed: {str(e)}")

    def extract_entities(self, text):
        try:
            return self.process(text)["ents"]
        except Exception as e:
            raise ValueError(f"Entity extraction failed: {str(e)}")