from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    day = models.DateField('day')
    public = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    lat = models.FloatField()
    lon = models.FloatField()


    def __str__(self):
        return self.title

class Skill(models.Model):
    skill = models.CharField(max_length=200)

    def __str__(self):
        return self.skill

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    avatar = models.ImageField()
