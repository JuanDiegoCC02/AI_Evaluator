
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from evaluator.models import Evaluation


class EvaluationAPITest(APITestCase):

    def test_create_evaluation(self):

        data = {
            "question": "What is Artificial Intelligence?",
            "answer": "Artificial Intelligence is the simulation of human intelligence by machines."
        }

        response = self.client.post(
            "/api/evaluations/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Evaluation.objects.count(),
            1
        )

        self.assertIn(
            "grammar_score",
            response.data
        )

        self.assertIn(
            "relevance_score",
            response.data
        )

        self.assertIn(
            "final_score",
            response.data
        )

        self.assertIn(
            "evaluation_label",
            response.data
        )