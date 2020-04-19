from src.word import Word


class Sentence:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words

    def get_values(self):
        return [word.value for word in self.words]

    def get_lemmas(self):
        return [word.lemma for word in self.words]

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass
