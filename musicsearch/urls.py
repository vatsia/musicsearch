from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^', views.index, name='index'),
    #url(r'^(?P<track_id>[0-9]+)/$', views.track, name='track'),
    #url(r'^(?P<artist_id>[0-9]+)/$', views.artist, name='artist'),
    url(r'^history/$', views.search_history, name='results'),
    url(r'^results/(?P<result_id>[0-9]+)/$', views.results, name='results'),
    url(r'^search/$', views.search_handler, name='search_handler'),
    url(r'^$', views.index, name='root'),
]