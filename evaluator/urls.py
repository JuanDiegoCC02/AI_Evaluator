from django.urls import path
from .views import EvaluationListCreateView
from .views import statistics_view


urlpatterns = [
    path(
        "evaluations/",
        EvaluationListCreateView.as_view(),
        name="evaluations"
    ),

    path(
        'statistics/',
        statistics_view,
        name='statistics'
    ),
]