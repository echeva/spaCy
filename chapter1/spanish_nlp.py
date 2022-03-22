# Import spaCy
import spacy

# Create the English nlp object
nlp = spacy.blank("es")

# Process a text
doc = nlp("¿Cómo estás?")

# Print the document text
print(doc.text)