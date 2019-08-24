from django.db import models
from django.utils import timezone
import datetime
from django.utils.timezone import now

class Publication(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=200)
    text = models.TextField(max_length=2000)
    date = models.DateField('date published', default=now)


    def __str__(self):
        return self.title
