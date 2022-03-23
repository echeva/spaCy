import spacy
from spacy.matcher import Matcher
from doc1 import text as text_1
from doc2 import text as text_2


def alias(matcher, doc, result):
    patterns = [[{"POS": "PROPN", "TEXT": {"REGEX": 'B\d{2}-\d{6}'}}]]
    matcher.add("ALIAS_PATTERN", patterns)
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["alias"] = doc[start:end]
        break


def entry_date(matcher, doc, result):
    patterns = [[{"POS": "NUM", "TEXT": {"REGEX": '\d{2}/\d{2}/\d{4}'}}]]
    matcher.add("DATE_PATTERN", patterns)
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["entry-date"] = doc[start:end]


def size(matcher, doc, result):
    pattern = [{"POS": "NUM", "TEXT": {"REGEX": '\d{1,}mm2'}}]
    matcher.add("SIZE_PATTERN", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["size"] = doc[start:end]


def ngs_biomarker(matcher, doc, result):
    result["ngs-biomarker"] = ''


def ngs_kit(matcher, doc, result):
    pattern = [{"LOWER": "oncomine"}, {"TEXT": {"REGEX": '\d{1,}'}}]
    # pattern = [{"LOWER": "oncomine", "POS": "VERB"}, {"TEXT": {"REGEX": '\d{1,}'}}]
    matcher.add("NGS_KIT_PATTERN", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["ngs-kit"] = doc[start:end]


def ngs_dna_alteration(matcher, doc, result):
    result["ngs-dna-alteration"] = ''


def ngs_position_alteration(matcher, doc, result):
    result["ngs-position-alteration"] = ''


def ngs_allelic_frequency(matcher, doc, result):
    patterns = [[{"LOWER": "frecuencia", "OP": "?"}, {"LOWER": "aproximada", "OP": "?"}, {"LOWER": "alelo"},
                 {"LOWER": "mutado", "OP": "?"}, {"POS": "SYM"}],
                [{"LOWER": "frecuencia"}, {"LOWER": "aproximada", "OP": "?"}, {"LOWER": "alelo"},
                 {"LOWER": "mutado", "OP": "?"}, {"POS": "NUM"}]]
    matcher.add("NGS_ALLELIC_FREQUENCY_PATTERN", patterns)
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["ngs-allelic-frequency"] = doc[end - 1:end]


def processing(nlp, text):
    doc = nlp(text)
    result = {}

    alias(Matcher(nlp.vocab), doc, result)
    entry_date(Matcher(nlp.vocab), doc, result)
    size(Matcher(nlp.vocab), doc, result)
    ngs_biomarker(Matcher(nlp.vocab), doc, result)
    ngs_kit(Matcher(nlp.vocab), doc, result)
    ngs_dna_alteration(Matcher(nlp.vocab), doc, result)
    ngs_position_alteration(Matcher(nlp.vocab), doc, result)
    ngs_allelic_frequency(Matcher(nlp.vocab), doc, result)

    return result


nlp = spacy.load("es_core_news_sm")
result_1 = processing(nlp, text_1)
result_2 = processing(nlp, text_2)
print(f"Archivo 1: {result_1}")
print(f"Archivo 2: {result_2}")

