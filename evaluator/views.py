from rest_framework import generics
from .models import Evaluation
from .serializers import EvaluationSerializer

from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class EvaluationListCreateView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


@api_view(['GET'])
def statistics_view(request):

    total = Evaluation.objects.count()

    average_score = Evaluation.objects.aggregate(
        Avg('final_score')
    )['final_score__avg'] or 0

    excellent = Evaluation.objects.filter(
        evaluation_label='Excellent'
    ).count()

    good = Evaluation.objects.filter(
        evaluation_label='Good'
    ).count()

    average = Evaluation.objects.filter(
        evaluation_label='Average'
    ).count()

    poor = Evaluation.objects.filter(
        evaluation_label='Poor'
    ).count()

    return Response({
        "total_evaluations": total,
        "average_score": round(average_score, 2),
        "excellent": excellent,
        "good": good,
        "average": average,
        "poor": poor
    })