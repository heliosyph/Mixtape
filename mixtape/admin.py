"""admin.py."""
from django.contrib import admin


from mixtape.models import User, Song, Playlist, Liked

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Liked)


# Register your models here.
