from __future__ import unicode_literals
import datetime
from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=256)

class Album(models.Model):
    name = models.CharField(max_length=256)
    release_date = models.DateTimeField()
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

class DataSearch(models.Model):
    keyword = models.CharField(max_length=128)
    search_time = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    user = mo

class SearchResult(models.Model):
    data_search_id = models.ForeignKey(DataSearch, on_delete=models.CASCADE)
    service = models.CharField(max_length=16)

class Track(models.Model):
    # search_result_id FK
    # artist_id FK
    # album_id FK
    search_result_id = models.ForeignKey(SearchResult, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    track_link = models.CharField(max_length=128)
    length = models.IntegerField()
    