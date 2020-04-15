"""
Django uses the model code to:
    (1) Create a DB schema
    (2) Create a Python DB-access API for accessing objects
"""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(r'date published')
    
    def __str__(self):
        """This method is used throughout Django's auto-generated admin."""
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """This method is used throughout Django's auto-generated admin."""
        return self.choice_text
