from evaluator.services.relevance import evaluate_relevance

score = evaluate_relevance(
    "What is Artificial Intelligence?",
    "Artificial Intelligence is the simulation of human intelligence by machines."
)

print(score)