from django.db import models

class MusicCard(models.Model):
    title = models.CharField(max_length=30)
    infoalbum = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    tracklist = models.TextField(blank=True) 