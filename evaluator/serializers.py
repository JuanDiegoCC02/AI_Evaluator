import time

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
        'evaluation_label',
        'processing_time',
        'language',
        'embedding_model',
        'grammar_errors',
        'response_length',
        )

    def create(self, validated_data):

        start_time = time.time()

        question = validated_data['question']
        answer = validated_data['answer']

        # Grammar evaluation
        grammar_result = evaluate_grammar(answer)

        grammar_errors = len(grammar_result['feedback'])

        response_length = len(answer.split())

        grammar_score = grammar_result['score']

        grammar_feedback = "\n".join(
            grammar_result['feedback']
        )
    

        # Semantic relevance
        relevance_score = evaluate_relevance(
            question,
            answer
        )

        processing_time = round(
            time.time() - start_time,
            3
        )

        # Final score
        final_score = round(
        grammar_score * 0.3 +
        relevance_score * 0.7,
        2
    )
        
        if final_score >= 90:
            evaluation_label = "Excellent"

        elif final_score >= 75:
            evaluation_label = "Good"

        elif final_score >= 60:
            evaluation_label = "Average"

        else:
            evaluation_label = "Poor"

        evaluation = Evaluation.objects.create(
            question=question,
            answer=answer,
            grammar_score=grammar_score,
            relevance_score=relevance_score,
            final_score=final_score,
            grammar_feedback=grammar_feedback,
            evaluation_label=evaluation_label,
            processing_time=processing_time,
            language="en-US",
            embedding_model="all-MiniLM-L6-v2",
            grammar_errors=grammar_errors,
            response_length=response_length
        )

        return evaluation