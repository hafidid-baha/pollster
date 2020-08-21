from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCAD)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerFiels(default=0)

    def __str__(self):
        return self.choise_text