from rest_framework import generics
from .models import Evaluation
from .serializers import EvaluationSerializer

# Create your views here.

class EvaluationListCreateView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    
