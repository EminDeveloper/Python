import spacy

nlp = spacy.load("en_core_web_md")

dog_embedding = nlp.vocab["Emin"].vector

type(dog_embedding)


dog_embedding.shape


print(dog_embedding[0:10])