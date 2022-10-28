from statistics import mode
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artiste_id=models.ForeignKey(Artiste,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    date_released=models.DateField
    likes=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_id=models.ForeignKey(Song,on_delete=models.CASCADE)
    content=models.CharField(max_length=400)

    def __str__(self):
        return self.content