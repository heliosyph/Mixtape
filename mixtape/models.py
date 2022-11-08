"""models.py."""
from django.db import models


class User(models.Model):
    """Model to keep info on users."""

    # primary key
    username_creator = models.CharField(max_length=200)

    # is the person added to friend list
    isFriend = models.BooleanField()

    # save the friend's name
    friend_name = models.CharField(max_length=100)

    # is friend a favorite?
    isFavoriteFriend = models.BooleanField()

    favorite_genre = models.CharField(max_length=200)
    favorite_artist = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    isFavoriteSong = models.BooleanField()

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

    def __str__(self):
        """Generate song name for model."""
        return self.song_name


class Playlist(models.Model):
    """Model to keep info on playlist."""

    # primary key
    playlist_name = models.CharField(max_length=200)

    song_name = models.ForeignKey(Song, on_delete=models.CASCADE)

    creator = models.ForeignKey(User, related_name="created_playlist", on_delete=models.CASCADE)
    likes = models.ForeignKey(User, related_name="likes_playlist", on_delete=models.CASCADE)

    isPrivate = models.BooleanField()
    playlist_description = models.CharField(max_length=200)

    def __str__(self):
        """Generate playlist name for model."""
        return self.playlist_name


class Liked(models.Model):
    """Model to keep info on liked association."""

    liked_playlist = models.BooleanField()
    username_creator = models.CharField(max_length=200)
    playlist_name = models.CharField(max_length=200)

    def __str__(self):
        """Generate liked name for model."""
        return self.liked_playlist


# Create your models here.
