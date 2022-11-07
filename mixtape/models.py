"""models.py."""
from django.db import models

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
    

# Create your models here.
