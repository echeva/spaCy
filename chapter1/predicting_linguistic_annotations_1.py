"""
Part 1
    Process the text with the nlp object and create a doc.
    For each token, print the token text, the token’s .pos_ (part-of-speech tag) and
    the token’s .dep_ (dependency label).
"""

import spacy

nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

for token in doc:
    # Get the token text, part-of-speech tag and dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # This is for formatting only
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

"""
Part 2
    Process the text and create a doc object.
    Iterate over the doc.ents and print the entity text and label_ attribute.
"""

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)

"""
Predeciting named entities  in context

Models are statistical and not always right. Whether their predictions are correct depends on the training data and the text you’re processing. Let’s take a look at an example.

    Process the text with the nlp object.
    Iterate over the entities and print the entity text and label.
    Looks like the model didn’t predict “iPhone X”. Create a span for those tokens manually.
"""

# Iterate over the entities
for ent in doc.ents:
    # Print the entity text and label
    print(ent.text, ent.label_)

# Get the span for "iPhone X"
iphone_x = doc[1:3]

# Print the span text
print("Missing entity:", iphone_x.text)