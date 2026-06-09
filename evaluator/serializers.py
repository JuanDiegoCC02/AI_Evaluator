from rest_framework import serializers
from .models import Evaluation

from .services.grammar import evaluate_grammar
from .services.relevance import evaluate_relevance


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluation
        fields = '__all__'
        read_only_fields = (
            'grammar_score',
            'relevance_score',
            'final_score',
            'grammar_feedback',
            'created_at',
        )

    def create(self, validated_data):

        question = validated_data['question']
        answer = validated_data['answer']

        # Grammar evaluation
        grammar_result = evaluate_grammar(answer)

        grammar_score = grammar_result['score']

        grammar_feedback = "\n".join(
            grammar_result['feedback']
        )

        # Semantic relevance
        relevance_score = evaluate_relevance(
            question,
            answer
        )

        # Final score
        final_score = (
        grammar_score * 0.3 +
        relevance_score * 0.7
    )

        evaluation = Evaluation.objects.create(
            question=question,
            answer=answer,
            grammar_score=grammar_score,
            relevance_score=relevance_score,
            final_score=final_score,
            grammar_feedback=grammar_feedback,
        )

        return evaluation