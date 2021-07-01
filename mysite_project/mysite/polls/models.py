from django.db import models


# Create your models here.
class Question(models.Model):
    pub_date      = models.DateTimeField('date published')
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return f"ID: {self.id} Question Text: {self.question_text}"

class Choice(models.Model):
    votes       = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
    question    = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return f"ID: {self.id} Choice Text: {self.choice_text}"

Question.objects.all() # should return an empty collection, which makes sense since we have nothing in the database yet. Let's create a question record.

from django.utils import timezone
question = Question(question_text="What's new?", pub_date=timezone.now())
question.save()
question.id
question.question_text
question.pub_date

question.question_text = 'What is up?'
question.save()

Question.objects.all()
## If you want to change the attributes, go ahead and overwrite them, then call save()
## Now if you wanted to get all the questions
