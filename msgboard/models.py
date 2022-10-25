from django.db import models
from django.utils import timezone


class Message(models.Model):
    authot = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)



# Create your models here.
