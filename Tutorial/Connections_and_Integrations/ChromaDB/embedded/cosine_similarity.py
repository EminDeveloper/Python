import numpy as np
import spacy
from cosine_similarity import compute_cosine_similarity

def compute_cosine_similarity(u: np.ndarray, v: np.ndarray) -> float:
    """Compute the cosine similarity between two vectors"""

    return (u @ v) / (np.linalg.norm(u) * np.linalg.norm(v))



nlp = spacy.load("en_core_web_md")

dog_embedding = nlp.vocab["dog"].vector
cat_embedding = nlp.vocab["cat"].vector
apple_embedding = nlp.vocab["apple"].vector
tasty_embedding = nlp.vocab["tasty"].vector
delicious_embedding = nlp.vocab["delicious"].vector
truck_embedding = nlp.vocab["truck"].vector

compute_cosine_similarity(dog_embedding, cat_embedding)


compute_cosine_similarity(delicious_embedding, tasty_embedding)


compute_cosine_similarity(apple_embedding, delicious_embedding)


compute_cosine_similarity(dog_embedding, apple_embedding)


compute_cosine_similarity(truck_embedding, delicious_embedding)