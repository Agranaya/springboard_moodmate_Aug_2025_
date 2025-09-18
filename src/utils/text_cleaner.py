# src/utils/text_cleaner.py

class TextCleaner:
    def __init__(self):
        pass

    def fit(self, X, y=None):
        """No fitting needed, return self"""
        return self

    def transform(self, X):
        """Clean a list of texts"""
        cleaned = []
        for text in X:
            if isinstance(text, str):
                text = text.lower().strip()
                # add more preprocessing if needed (remove punctuation, etc.)
            cleaned.append(text)
        return cleaned
