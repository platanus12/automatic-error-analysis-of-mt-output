class Word:
    def __init__(self, value: str, lemma: str):
        self.value = value
        if lemma == '_':
            self.lemma = None
        else:
            self.lemma = lemma

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.value == other.value and self.lemma == other.lemma
