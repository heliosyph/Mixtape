"""Accounts models."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


from django.contrib.postgres.fields import ArrayField

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """A custom User model.

    Arguments:
    ---------
    AbstractUser : class
        Django's `AbstractUser` class.

    Returns:
    -------
    object:
        `CustomUser` model.

    """

    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        """Get the string representation of the object.

        Returns:
        -------
        str
            The unique identifer of the model, `email`.

        """
        return self.email



# mixtape database code
class Song(models.Model):
    # primary key
    song_name = models.CharField(max_length = 200)

    song_length = models.DurationField()
    artist_name = models.CharField(max_length = 200)
    song_genre = models.CharField(max_length = 200)
    album = models.CharField(max_length = 200)

    def __str__(self):
        return self.song_name

class User(models.Model):
    #primary key
    username_creator = models.CharField(max_length = 200)
    #primary key
    liked_playlist =models.BooleanField()

    created_playlist = models.BooleanField()

    #is the person added to friend list
    isFriend = models.BooleanField()

    #save the friend's name
    friend_name = models.CharField(max_length = 100)

    #is friend a favorite?
    isFavoriteFriend = models.BooleanField()

    favorite_genre = models.CharField(max_length = 200)
    favorite_artist = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200)
    isFavoriteSong = models.BooleanField()

    def __str__(self):
        return self.username_creator

class Playlist(models.Model):
    #primary key
    playlist_name = models.CharField(max_length = 200)

    song_name = models.ForeignKey(Song, on_delete = models.CASCADE)
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ForeignKey(User, on_delete = models.CASCADE)

    isPrivate = models.BooleanField()
    playlist_description = models.CharField(max_length = any)

    def __str__(self):
        return self.playlist_name

#another table because of the many to many relationship
class Liked(models.Model):
    liked_playlist = models.BooleanField()
    username_creator = models.CharField(max_length = 200)
    playlist_name = models.CharField(max_length = 200)




    def __str__(self):
        return self.liked_playlist
    



    

