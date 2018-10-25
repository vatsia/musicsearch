from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Artist, Track, DataSearch, Album, SearchResult
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404

# Youtube Data API imports
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import datetime

#spotipy imports
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
#import pprint

# renders search bar
def index(request):
    return render(request, 'musicsearch/search.html')

# makes actual search from various services and redirects to search results
def search_handler(request):
    searchobj = DataSearch.objects.create(keyword=request.POST['keyword'])
    # make searches here
    search_youtube(request.POST['keyword'], searchobj)
    search_spotify(request.POST['keyword'], searchobj)
    return HttpResponseRedirect('/musicsearch/results/' + str(searchobj.id))

# render search result page
def results(request, result_id):
    context = {}
# HAE DATASEARCHIT MOLEMMISTA PALVELUISTA JA NIILLA VASTA TRACKIT
    datasearch = DataSearch.objects.get(id=result_id)
    
    result_list = get_list_or_404(SearchResult, data_search_id=datasearch.id)
        context['tracks'] = ()
    for(result in result_list)
        context['tracks'].append() get_list_or_404(Track, search_result_id=result.id)
    
    return render(request, 'musicsearch/results.html', context)

def search_youtube(keyword, ds_id):
    DEVELOPER_KEY = "AIzaSyBcUxRjftWVZdtrhKrvhbUxnTQ6Jzbd7SA"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=keyword, part="id,snippet", maxResults=10).execute()

    serres = SearchResult.objects.create(data_search_id=ds_id, service='youtube')
    
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            artist = search_result["snippet"]["title"].split(' - ', 1)[0]
            track_name = search_result["snippet"]["title"].split(' - ', 1)[0]
            
            # fallback if artist name parsing fails
            if track_name == '':
                track_name = search_result["snippet"]["title"]
            
            art = Artist.objects.create(name=artist)
            alb = Album.objects.create(name=track_name, release_date=datetime.datetime.min, artist_id=art)
            Track.objects.create(
                artist_id = art,
                album_id = alb,
                search_result_id = serres,
                name=search_result['snippet']['title'], 
                track_link="https://www.youtube.com/watch?v=" + search_result["id"]["videoId"],
                length=0
            )
            
            


def search_spotify(keyword, ds_id):
    client_id = "53e6b264343d4b8fb20413ac75eaf7ac"
    client_secret = "a6b7a2afac2a45e798c0749541f9f2a1"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp_search_result = sp.search(q=keyword, type='track', market='FI', limit='10')
    sp_serres = SearchResult.objects.create(data_search_id=ds_id, service='spotify')
    
    for track in sp_search_result['tracks']['items'][:10]:
        sp_artist = track['artists'][0]['name']
        sp_track = track['name']
        sp_link = track['external_urls']['spotify']
        sp_releasedate = track['album']['release_date']
        sp_album = track['album']['name']
        sp_duration = track['duration_ms']
        
        art = Artist.objects.create(name=sp_artist)
        alb = Album.objects.create(name=sp_track, release_date=sp_releasedate + " 00:00", artist_id=art)
        Track.objects.create(
                artist_id = art,
                album_id = alb,
                search_result_id = sp_serres,
                name = sp_track, 
                track_link = sp_link,
                length = sp_duration 
                )
            
#   result = sp.search(keyword)
#   context['result'] = 
#   return render(request, 'musicsearch/spresults.html', context)