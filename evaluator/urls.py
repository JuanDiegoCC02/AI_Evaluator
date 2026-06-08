from django.urls import path
from .views import EvaluationListCreateView


urlpatterns = [
    path(
        "evaluations/",
        EvaluationListCreateView.as_view(),
        name="evaluations"
    ),
]