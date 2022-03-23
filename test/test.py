import spacy
from spacy.matcher import Matcher
from doc2 import text

nlp = spacy.load("es_core_news_sm")
doc = nlp(text)

result = {}


def alias(matcher, doc):
    pattern = [{"POS": "PROPN", "LENGTH": {"==": 10}, "TEXT": {"REGEX": 'B\d{2}-\d{6}'}}]
    matcher.add("ALIAS_PATTERN", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["alias"] = doc[start:end]


def entry_date(matcher, doc):
    for token in doc:
        if token.pos_ == "NUM":
            if "/" in token.text and len(token.text) == 10:
                result["entry-date"] = token.text


def size(matcher, doc):
    pattern = [{"POS": "NUM", "TEXT": {"REGEX": '\d{1,}mm2'}}]
    matcher.add("SIZE_PATTERN", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["size"] = doc[start:end]


def ngs_biomarker(matcher, doc):
    result["ngs-biomarker"] = ''


def ngs_kit(matcher, doc):
    pattern = [{"LOWER": "oncomine"}, {"TEXT": {"REGEX": '\d{1,}'}}]
    # pattern = [{"LOWER": "oncomine", "POS": "VERB"}, {"TEXT": {"REGEX": '\d{1,}'}}]
    matcher.add("NGS_KIT_PATTERN", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["ngs-kit"] = doc[start:end]


def ngs_dna_alteration(matcher, doc):
    result["ngs-dna-alteration"] = ''


def ngs_position_alteration(matcher, doc):
    result["ngs-position-alteration"] = ''


def ngs_allelic_frequency(matcher, doc):
    pattern = [{"POS": "SYM"}]
    matcher.add("NGS_ALLELIC_FREQUENCY_PATTERN", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        result["ngs-allelic-frequency"] = doc[start:end]


for token in doc:
    print(token.text, token.pos_)

alias(Matcher(nlp.vocab), doc)
entry_date(Matcher(nlp.vocab), doc)
size(Matcher(nlp.vocab), doc)
ngs_biomarker(Matcher(nlp.vocab), doc)
ngs_kit(Matcher(nlp.vocab), doc)
ngs_dna_alteration(Matcher(nlp.vocab), doc)
ngs_position_alteration(Matcher(nlp.vocab), doc)
ngs_allelic_frequency(Matcher(nlp.vocab), doc)


print(result)
