"""admin.py."""
from django.contrib import admin

from mixtape.models import Playlist, Song, User

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Playlist)

# Register your models here.
