from django.urls import path
from .views import EvaluationListCreateView


urlspatterns = [
    path(
        "evaluations/",
        EvaluationListCreateView.as_view(),
        name="evaluations"
    ),
]