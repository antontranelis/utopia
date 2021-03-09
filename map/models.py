from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_text = models.TextField()
    event_start = models.DateTimeField('event start')
    event_end = models.DateTimeField('event end')


    def __str__(self):
        return self.event_title
