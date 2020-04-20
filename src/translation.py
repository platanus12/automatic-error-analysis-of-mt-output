from collections import Counter

from src.sentence import Sentence


class Translation:
    def __init__(self, reference: Sentence = None, hypothesis: Sentence = None):
        self.r = reference
        self.h = hypothesis

    def count_all_lemmas(self):
        lemmas = Counter(
            [word.lemma for word in self.r.words if word.lemma != "_"] +
            [word.lemma for word in self.h.words if word.lemma != "_"]
        )
        return lemmas

    def remove_correct_translation(self):
        potential_r_errors = [word for word in self.r.words if word not in self.h.words]
        potential_h_errors = [word for word in self.h.words if word not in self.r.words]
        self.r.words = potential_r_errors
        self.h.words = potential_h_errors
