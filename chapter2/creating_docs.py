"""
    Import the Doc from spacy.tokens.
    Create a Doc from the words and spaces. Don’t forget to pass in the vocab!
"""

import spacy

nlp = spacy.blank("en")

# Import the Doc class
from spacy.tokens import Doc, Span

# Desired text: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Desired text: "Go, get started!"
words = ["Go", ",", "get", "started", "!"]
spaces = [False, True, True, False, False]

# Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

"""
    Import the Doc from spacy.tokens.
    Complete the words and spaces to match the desired text and create a doc.
"""

# Desired text: "Oh, really?!"
words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

# Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

"""
In this exercise, you’ll create the Doc and Span objects manually, 
and update the named entities – just like spaCy does behind the scenes. 
A shared nlp object has already been created.
    Import the Doc and Span classes from spacy.tokens.
    Use the Doc class directly to create a doc from the words and spaces.
    Create a Span for “David Bowie” from the doc and assign it the label "PERSON".
    Overwrite the doc.ents with a list of one entity, the “David Bowie” span.
"""
words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Create a doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Create a span for "David Bowie" from the doc and assign it the label "PERSON"
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# Add the span to the doc's entities
doc.ents = [span]

# Print entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])