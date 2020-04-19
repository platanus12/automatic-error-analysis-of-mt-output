from conllu import parse_incr
from collections import Counter
from src.sentence import Sentence
from src.translation import Translation
from src.word import Word


def count_inflectional_errors(translation):
    errors = 0
    translation.remove_correct_translation()
    lemmas = translation.count_all_lemmas()
    # removes single lemmas because they cant point to inflectional errors)
    for word, count in list(lemmas.items()):
        if count == 1:
            lemmas.subtract(Counter([word]))

    r_lemmas = translation.r.get_lemmas()
    h_lemmas = translation.h.get_lemmas()
    for lemma in set(lemmas.elements()):
        if lemma in r_lemmas:
            if lemma in h_lemmas:
                errors += min(r_lemmas.count(lemma), h_lemmas.count(lemma))
            else:
                errors += r_lemmas.count(lemma)
        else:
            continue
        # elif lemma in h_lemmas:
        #     errors += h_lemmas.count(lemma)
        # else:
        #     raise ValueError("lemma not found")
    return errors


# TODO: change name
def calc_inflectional_error_rate(translations):
    inflectional_errors = 0
    words_in_reference = 0
    for translation in translations:
        words_in_reference += len(translation.r.words)
        inflectional_errors += count_inflectional_errors(translation)
    infer_percent = inflectional_errors / words_in_reference * 100

    print("{:.2f}".format(infer_percent))


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


if __name__ == '__main__':
    translation_outputs = read_conllu_outputs(r"D:\lingo\HebPipe\result.txt", r"D:\lingo\HebPipe\some.txt")
    calc_inflectional_error_rate(translation_outputs)
