from django.db import models

class To_Do(models.Model):
    text = models.TextField(max_length=200)
    complete = models.BooleanField(default=False)

class Step(models.Model):
    to_do_id = models.ForeignKey('todo.To_Do', on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    complete = models.BooleanField(default=False)
