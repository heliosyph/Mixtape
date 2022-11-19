"""models.py."""
from django.db import models

from users.models import CustomUser


class User(models.Model):
    """Model to keep info on users."""

    # primary key
    username_creator = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # save the friend's name
    friend_name = models.CharField(max_length=100)

    favorite_genre = models.CharField(max_length=200)
    favorite_artist = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    # isFavoriteSong = models.BooleanField()

    def __str__(self):
        """Generate name for model."""
        return self.username_creator


class Song(models.Model):
    """Model to keep info on songs."""

    # primary key
    song_name = models.CharField(max_length=200)

    song_length = models.DurationField()
    artist_name = models.CharField(max_length=200)
    song_genre = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    likes = models.ManyToManyField(User)
    isFavoriteSong = models.BooleanField()

    def __str__(self):
        """Generate song name for model."""
        return self.song_name


class Playlist(models.Model):
    """Model to keep info on playlist."""

    # primary key
    playlist_name = models.CharField(max_length=200)

    # song_name = models.ForeignKey(Song, on_delete=models.CASCADE)

    creator = models.ForeignKey(User, related_name="created_playlist", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User)
    songs = models.ManyToManyField(Song)

    isPrivate = models.BooleanField()
    playlist_description = models.CharField(max_length=200)

    def __str__(self):
        """Generate playlist name for model."""
        return self.playlist_name


# Create your models here.
