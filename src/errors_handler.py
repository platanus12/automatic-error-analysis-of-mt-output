from collections import Counter
from src.translation import Translation


def count_inflectional(translation):
    number_of_errors = 0
    translation.remove_correct_translation()
    lemmas = translation.count_all_lemmas()
    for word, count in list(lemmas.items()):
        if count == 1:
            lemmas.subtract(Counter([word]))

    r_lemmas = translation.r.get_lemmas()
    h_lemmas = translation.h.get_lemmas()
    for lemma in set(lemmas.elements()):
        number_of_errors += min(r_lemmas.count(lemma), h_lemmas.count(lemma))
    return number_of_errors


def count_reordering(translation):
    return 0


class ErrorsHandler:
    def __init__(self):
        self.errors = {}

    def _count_errors(self, translations: [Translation]):
        counter = Counter()
        for translation in translations:
            counter.update(Counter({
                'inflectional': count_inflectional(translation),
                'reordering': count_reordering(translation)
            }))
        self.errors['all'] = sum(counter.values())
        self.errors.update(counter)

    def get_errors(self, translations: [Translation]) -> dict:
        self._count_errors(translations)
        if self.errors['all'] == 0:
            return self.errors
        else:
            for key in self.errors.keys():
                if key != 'all':
                    self.errors[key] = self.errors[key] / self.errors['all'] * 100
            return self.errors
