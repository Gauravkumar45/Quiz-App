from django.db import models
from django.utils.translation import gettext_lazy as _

class Quizze(models.Model):
    ques = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.ques


class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    quiz = models.ForeignKey(Quizze, related_name='question', on_delete=models.DO_NOTHING)
    ques = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(Updated):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=100)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text