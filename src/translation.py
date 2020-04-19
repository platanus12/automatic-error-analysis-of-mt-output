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
        for r_word in self.r.words:
            for h_word in self.h.words:
                if r_word == h_word:
                    self.h.words.remove(h_word)
                    self.r.words.remove(r_word)
