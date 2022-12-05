"""Tests for `users` app."""
from datetime import timedelta
from http import HTTPStatus

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
    """Testing user delete view."""

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
    """Testing user update view."""

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
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

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

        query = Playlist.objects.get(playlist_name="pop")
        self.assertEqual(playlist, query)


class PlaylistCreateViewTestCase(TestCase):
    """Testing playlist create view."""

    @parameterized.expand(
        [
            (
                {
                    "playlist_name": "pop",
                    "songs": "song",
                    "likes": "John Doe",
                    "isPrivate": False,
                    "playlist_description": "this is cool",
                },
                HTTPStatus.FOUND,
            ),
        ]
    )
    def test_playlist_create_view(self, params, status_code):
        """Test Playlist create view with all information."""

        playlist_create_url = reverse("mixtape:playlist_create")
        response = self.client.post(playlist_create_url, data=params)
        self.assertEqual(response.status_code, status_code)


class PlaylistUpdateViewTestCase(TestCase):
    """Testing playlist update view."""

    @parameterized.expand(
        [
            (
                {
                    "playlist_name": "cooler pop",
                    "songs": "song",
                    "likes": "John Doe",
                    "isPrivate": True,
                    "playlist_description": "this is cooler",
                },
                HTTPStatus.FOUND,
            ),
        ]
    )
    def test_playlist_update_view(self, params, status_code):
        """Test Playlist Update view with all information."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

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

        playlist_update_url = reverse("mixtape:playlist_update", args=[playlist.pk])
        response = self.client.post(playlist_update_url, data=params)
        self.assertEqual(response.status_code, status_code)


class PlaylistDeleteViewTestCase(TestCase):
    """Testing playlist delete view."""

    def test_playlist_delete_view_get_request(self):
        """Test Playlist Delete view."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

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

        message_for_playlist_delete = self.client.delete(
            reverse("mixtape:playlist_delete", args=[playlist.pk])
        )
        self.assertEqual(message_for_playlist_delete.status_code, HTTPStatus.FOUND)
        with pytest.raises(NoReverseMatch) as exc_info:
            self.client.delete(reverse("mixtape:Playlist", args=[playlist.pk]))
        self.assertEqual(exc_info.type, NoReverseMatch)


class SongTestCase(TestCase):
    """Tests for `Song` model."""

    def test_create(self):
        """Tests if `Song`'s `create()` method is working using a query."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

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

        self.assertTrue(isinstance(song, Song))
        self.assertEqual(str(song), "song")


class SongCreateViewTestCase(TestCase):
    """Testing song create view."""

    @parameterized.expand(
        [
            (
                {
                    "song_name": "song",
                    "song_length": timedelta(minutes=3, seconds=26),
                    "artist_name": "coolguy",
                    "song_genre": "pop",
                    "album": "cool songs",
                    "likes": "John Doe",
                    "isFavoriteSong": False,
                },
                HTTPStatus.FOUND,
            ),
        ]
    )
    def test_song_create_view(self, params, status_code):
        """Test Song create view with all information."""

        song_create_url = reverse("mixtape:song_create")
        response = self.client.post(song_create_url, data=params)
        self.assertEqual(response.status_code, status_code)


class SongUpdateViewTestCase(TestCase):
    """Testing Song update view."""

    @parameterized.expand(
        [
            (
                {
                    "song_name": "cooler song",
                    "song_length": timedelta(minutes=3, seconds=27),
                    "artist_name": "coolerguy",
                    "song_genre": "cool pop",
                    "album": "cooler songs",
                    "likes": "John Doe",
                    "isFavoriteSong": True,
                },
                HTTPStatus.FOUND,
            ),
        ]
    )
    def test_song_update_view(self, params, status_code):
        """Test Song update view."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

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

        song_update_url = reverse("mixtape:song_update", args=[song.pk])
        response = self.client.post(song_update_url, data=params)
        self.assertEqual(response.status_code, status_code)


class SongDeleteViewTestCase(TestCase):
    """Testing Song delete view."""

    def test_song_delete_view_get_request(self):
        """Test Song Delete view."""
        CustomUser.objects.create_user(email="jdoe@gmail.com", password="password123")

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

        message_for_song_delete = self.client.delete(reverse("mixtape:song_delete", args=[song.pk]))
        self.assertEqual(message_for_song_delete.status_code, HTTPStatus.FOUND)
        with pytest.raises(NoReverseMatch) as exc_info:
            self.client.delete(reverse("mixtape:Song", args=[song.pk]))
        self.assertEqual(exc_info.type, NoReverseMatch)
