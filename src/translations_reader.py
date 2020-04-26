from src.word import Word
from conllu import parse_incr
from src.sentence import Sentence
from src.translation import Translation


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


def parse_segment(segment):
    sentence = Sentence()
    words_segment = segment.split('. ')
    values = words_segment[0].split()
    lemmas = words_segment[1].split()
    for value, lemma in zip(values, lemmas):
        sentence.words.append(Word(value, lemma))
    return sentence


def read_files(ref_path, hyp_path):
    translations = []
    with open(ref_path, 'r', encoding='utf-8') as ref, open(hyp_path, 'r', encoding='utf-8') as hyp:
        for r_segment, h_segment in zip(ref, hyp):
            ref_sentence = parse_segment(r_segment)
            hyp_sentence = parse_segment(h_segment)
            translations.append(Translation(ref_sentence, hyp_sentence))
    return translations