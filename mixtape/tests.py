"""Tests for `users` app."""
from ast import Delete
from datetime import timedelta
from http import HTTPStatus
from re import M
from telnetlib import STATUS
from venv import create

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import NoReverseMatch, reverse
from parameterized import parameterized

from mixtape.models import Playlist, Song, User
from users.models import CustomUser


class UserTestCase(TestCase):
    """Test Cases for User Model."""

    def test_create_User(self):
        """Test to create a user."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

        user1 = User.objects.create(
            username_creator="John Doe",
            user_id=1,
            friend_name="Johnny",
            favorite_genre="Hip-Hop/Rap",
            favorite_artist="Metro Boomin",
            status="Online",
        )
        self.assertTrue(isinstance(user1, User))
        query = User.objects.get(username_creator="John Doe")
        self.assertEqual(user1, query)

    def test_create_User_with_missing_information(self):
        """Test User Create view with missing information."""
        with pytest.raises(IntegrityError) as exc_info:
            User.objects.create(
                username_creator="John Doe",
                user_id=1,
                friend_name=None,
                favorite_genre="Hip-Hop/Rap",
                favorite_artist="Metro Boomin",
                status="Online",
            )
        self.assertEqual(exc_info.type, IntegrityError)


class UserCreateViewTestCase(TestCase):
    """Testing user create view."""

    @parameterized.expand(
        [
            (
                {
                    "username_creator": "john doe",
                    "user_id": "1",
                    "friend_name": "Johnny",
                    "favorite_genre": "Hip-Hop/Rap",
                    "favorite_artist": "Metro Boomin",
                    "status": "Online",
                },
                HTTPStatus.FOUND,
            ),
        ]
    )
    def test_user_create_view(self, params, status_code):
        """Test User Create view with all information."""
        user_create_url = reverse("mixtape:User_create")
        response = self.client.post(user_create_url, data=params)
        self.assertEqual(response.status_code, status_code)


class UserDeleteViewTestCase(TestCase):
    """Testing user create view."""

    def test_user_delete_view_get_request(self):
        """Test User Delete view."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

        user = User.objects.create(
            username_creator="John Doe",
            user_id=1,
            friend_name="Johnny",
            favorite_genre="Hip-Hop/Rap",
            favorite_artist="Metro Boomin",
            status="Online",
        )
        message_for_user_delete = self.client.delete(
            reverse("mixtape:User_delete", args=[user.user_id])
        )
        self.assertEqual(message_for_user_delete.status_code, HTTPStatus.FOUND)
        with pytest.raises(NoReverseMatch) as exc_info:
            self.client.delete(reverse("mixtape:User", args=[user.user_id]))
        self.assertEqual(exc_info.type, NoReverseMatch)


class UserUpdateViewTestCase(TestCase):
    """Testing user create view."""

    @parameterized.expand(
        [
            (
                {
                    "username_creator": "john doe",
                    "user_id": "1",
                    "friend_name": "Johnny Boy",
                    "favorite_genre": "Hip-Hop/Rap",
                    "favorite_artist": "Kendrick Lamar",
                    "status": "Online",
                },
                HTTPStatus.FOUND,
            ),
        ]
    )
    def test_user_update_view(self, params, status_code):
        """Test User Update view with all information."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

        user = User.objects.create(
            username_creator="John Doe",
            user_id=1,
            friend_name="Johnny",
            favorite_genre="Hip-Hop/Rap",
            favorite_artist="Metro Boomin",
            status="Online",
        )
        user_update_url = reverse("mixtape:User_update", args=[user.user_id])
        response = self.client.post(user_update_url, data=params)
        self.assertEqual(response.status_code, status_code)


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
