from sentence_transformers import SentenceTransformer

model = SentenceTransformer("nomic-ai/nomic-embed-text-v1")


def generate_embedding(text):

    embedding = model.encode(text)

    return embedding.tolist()