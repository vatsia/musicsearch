from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^', views.index, name='index'),
    #url(r'^(?P<track_id>[0-9]+)/$', views.track, name='track'),
    #url(r'^(?P<artist_id>[0-9]+)/$', views.artist, name='artist'),
    url(r'^(?P<search_id>[0-9]+)/$', views.search, name='search'),
    url(r'^spotify/(?P<keyword>[0-9a-zA-Z]+)/$', views.search_spotify, name='search_spotify'),
]










