# Import spaCy
import spacy

# Create a blank English nlp object
nlp = spacy.blank("en")
# Created by processing a string of text with the nlp object
doc = nlp("Hello world!")
# nlp = spacy.load("en_core_web_sm")

# Iterate over tokens in a Doc
for token in doc:
    print(token.text)

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)

# A slice from the Doc is a Span object
span = doc[1:3]

# Get the span text via the .text attribute
print(span.text)

doc = nlp("It costs $5.")
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])