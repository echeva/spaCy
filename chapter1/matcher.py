import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)

# Iterate over the matches
"""
Each tuple consists of three values: the match ID, 
the start index and the end index of the matched span.
"""
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

# Matching lexical attributes

pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]

doc = nlp("2018 FIFA World Cup: France won!")

matcher.add("LEXICAL_PATTERN", [pattern])
matches = matcher(doc)

for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]

doc = nlp("I loved dogs but now I love cats more.")

matcher.add("LOVE_PATTERN", [pattern])
matches = matcher(doc)
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

"""
Operators and quantifiers let you define how often a token should be matched. They can be added 
using the "OP" key.

Here, the "?" operator makes the determiner token optional, so it will match a token with the 
lemma "buy", an optional article and a noun.

"""
pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]

doc = nlp("I bought a smartphone. Now I'm buying apps.")

matcher.add("OPTIONAL_PATTERN", [pattern])
matches = matcher(doc)
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)


"""
"OP" can have one of four values:
An "!" negates the token, so it's matched 0 times.
{"OP": "!"} 	Negation: match 0 times

A "?" makes the token optional, and matches it 0 or 1 times.
{"OP": "?"} 	Optional: match 0 or 1 times

A "+" matches a token 1 or more times.
{"OP": "+"} 	Match 1 or more times

And finally, an "*" matches 0 or more times.
{"OP": "*"} 	Match 0 or more times
"""

# Let's practice!
nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with the shared vocabulary
matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{"TEXT": "iPhone"},
          {"TEXT": "X"}]

# Add the pattern to the matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use the matcher on the doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])