from django.contrib import admin
from .models import Track, SearchResult, DataSearch, Album, Artist
# Register your models here.

admin.site.register(Track)
admin.site.register(SearchResult)
admin.site.register(DataSearch)
admin.site.register(Album)
admin.site.register(Artist)