from django.db import models

# Create your models here.

#model for evaluation 
class Evaluation(models.Model):
    question = models.TextField()
    answer = models.TextField()

    grammar_score = models.FloatField(default=0)  
    relevance_score = models.FloatField(default=0)
    final_score = models.FloatField(default=0)

    grammar_feedback = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    evaluation_label = models.CharField(max_length=20, default="Unknown")
    
    def __str__(self):
        return f"Evaluation {self.id}"