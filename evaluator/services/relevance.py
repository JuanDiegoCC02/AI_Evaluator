from sentence_transformers import SentenceTransformer
from sentence_transformers import util

# Cargar modelo una sola vez
model = SentenceTransformer("all-MiniLM-L6-v2")


def evaluate_relevance(question, answer):
    """
    Calcula la similitud semántica entre pregunta y respuesta.
    Retorna un score de 0 a 100.
    """

    question_embedding = model.encode(
        question,
        convert_to_tensor=True
    )

    answer_embedding = model.encode(
        answer,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        question_embedding,
        answer_embedding
    )

    score = round(
        similarity.item() * 100,
        2
    )

    return score