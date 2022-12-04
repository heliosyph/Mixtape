"""Tests for `users` app."""
from datetime import timedelta
from http import HTTPStatus
from re import M

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized
from platformdirs import user_runtime_dir

from mixtape.models import Playlist, Song, User
from users.models import CustomUser


class UserTestCase(TestCase):
    """Test Cases for User Model."""

    def test_create_User(self):
        """Test to create a user."""
        customuser = CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

        user = User.objects.create(
            username_creator="John Doe",
            user_id=1,
            friend_name="Johnny",
            favorite_genre="Hip-Hop/Rap",
            favorite_artist="Metro Boomin",
            status="Online",
        )
        self.assertTrue(isinstance(customuser, CustomUser))
        self.assertEqual(str(customuser), "jdoe@gmail.com")
        self.assertTrue(isinstance(user, User))
        query = User.objects.get(username_creator="John Doe")
        self.assertEqual(user, query)


class PlaylistTestCase(TestCase):
    """Tests for `Playlist` model."""

    def test_create(self):
        """Tests if `Playlist`'s `create()` method is working using a query."""
        customuser = CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

        user = User.objects.create(
            username_creator="John Doe",
            user_id=1,
            friend_name="Johnny",
            favorite_genre="Hip-Hop/Rap",
            favorite_artist="Metro Boomin",
            status="Online",
        )
        song = Song.objects.create(
            song_name="song",
            song_length=timedelta(minutes=3, seconds=26),
            artist_name="coolguy",
            song_genre="pop",
            album="cool songs",
            isFavoriteSong=False,
        )
        song.likes.add(user)
        playlist = Playlist.objects.create(
            playlist_name="pop",
            creator=user,
            isPrivate=False,
            playlist_description="this is cool",
        )  # not sure how likes and songs would work here (manytomanyfields)
        playlist.likes.add(user)
        playlist.songs.add(song)

        self.assertTrue(isinstance(customuser, CustomUser))
        self.assertEqual(str(customuser), "jdoe@gmail.com")
        query = Playlist.objects.get(playlist_name="pop")
        self.assertEqual(playlist, query)


class SongTestCase(TestCase):
    """Tests for `Song` model."""

    def test_create(self):
        """Tests if `Song`'s `create()` method is working using a query."""
        customuser = CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

        user = User.objects.create(
            username_creator="John Doe",
            user_id=1,
            friend_name="Johnny",
            favorite_genre="Hip-Hop/Rap",
            favorite_artist="Metro Boomin",
            status="Online",
        )
        song = Song.objects.create(
            song_name="song",
            song_length=timedelta(minutes=3, seconds=26),
            artist_name="coolguy",
            song_genre="pop",
            album="cool songs",
            isFavoriteSong=False,
        )
        song.likes.add(user)

        self.assertTrue(isinstance(customuser, CustomUser))
        self.assertEqual(str(customuser), "jdoe@gmail.com")
        self.assertTrue(isinstance(song, Song))
        self.assertEqual(str(song), "song")
