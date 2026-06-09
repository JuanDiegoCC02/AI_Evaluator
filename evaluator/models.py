from django.db import models

# Create your models here.

#model for evaluation 
from django.db import models

class Evaluation(models.Model):
    question = models.TextField()
    answer = models.TextField()

    grammar_score = models.FloatField(default=0)
    relevance_score = models.FloatField(default=0)
    final_score = models.FloatField(default=0)

    evaluation_label = models.CharField(max_length=20, default="Unknown")

    grammar_feedback = models.TextField(blank=True)

    processing_time = models.FloatField(default=0)

    language = models.CharField(max_length=10,default="en-US")

    embedding_model = models.CharField(max_length=100, default="all-MiniLM-L6-v2")

    grammar_errors = models.IntegerField(default=0)

    response_length = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluation {self.id}"