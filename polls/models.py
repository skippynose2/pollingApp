import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

#creating a class which we can add to the database
#visit this url to understand more https://docs.djangoproject.com/en/3.1/intro/tutorial02/

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.question_text

    def was_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    # Foreignkey tells Django each choice is related to one question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_texts = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_texts
