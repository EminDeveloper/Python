from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
texts = [
         "The canine barked loudly.",
         "The dog made a noisy bark.",
         "He ate a lot of pizza.",
         "He devoured a large quantity of pizza pie.",
]

text_embeddings = model.encode(texts)

type(text_embeddings)


text_embeddings.shape