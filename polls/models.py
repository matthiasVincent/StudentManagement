from django.db import models

# Create your models here.
class Question(models.Model):
    ques_text = models.CharField(max_length=200)
    pub_date= models.DateTimeField("date_published")

    def __str__(self):
        return "{}".format(self.ques_text)

class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    vote = models.IntegerField(default=0)
    quest = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.choice_text)