from conllu import parse_incr
from collections import Counter
from src.sentence import Sentence
from src.translation import Translation
from src.word import Word


def count_inflectional_errors(translation):
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


def get_errors_scores(translations):
    number_of_errors = 0
    inflectional_errors = 0
    for translation in translations:
        inflectional_errors += count_inflectional_errors(translation)
    number_of_errors = inflectional_errors
    print(f"number of inflectional errors: {inflectional_errors}")
    print(f"percentage of inflectional errors from all errors: {inflectional_errors / number_of_errors * 100}")


# TODO: separate reading files from parsing text
def read_conllu_outputs(reference_path, hypothesis_path):
    translations = []
    with open(reference_path, 'r', encoding="utf-8") as ref, open(hypothesis_path, 'r', encoding="utf-8") as hyp:
        for ref_tokenlist, hyp_tokenlist in zip(parse_incr(ref), parse_incr(hyp)):
            ref_sentence = Sentence()
            hyp_sentence = Sentence()
            for token in ref_tokenlist:
                ref_sentence.words.append(Word(token["form"], token["lemma"]))
            for token in hyp_tokenlist:
                hyp_sentence.words.append(Word(token["form"], token["lemma"]))
            translations.append(Translation(ref_sentence, hyp_sentence))
    return translations


def read_files(ref_path, hyp_path):
    pass


if __name__ == '__main__':
    translation_outputs = read_conllu_outputs(r"D:\lingo\HebPipe\result.txt", r"D:\lingo\HebPipe\some.txt")
    # translation_outputs_test = read_files("", "")
    get_errors_scores(translation_outputs)
    # calc_inflectional_error_rate(translation_outputs_test)
