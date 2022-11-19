"""views.py."""
from django.shortcuts import render
from django.views import generic

from mixtape.models import Playlist, Song, User


class PlaylistListView(generic.ListView):
    """Playlist List class."""

    model = Playlist
    template_name = "mixtape/playlist_list.html"  # file name is lower case


class PlaylistDetailView(generic.DetailView):
    """Playlist Detail class."""

    model = Playlist
    template_name = "mixtape/playlist_detail.html"  # file name is lower case


class SongListView(generic.ListView):
    """Song List class."""

    model = Song
    template_name = "mixtape/song_list.html"  # file name is lower case


class SongDetailView(generic.DetailView):
    """Song Detail class."""

    model = Song
    template_name = "mixtape/song_detail.html"  # file name is lower case


class UserListView(generic.ListView):
    """User List class."""

    model = User
    template_name = "mixtape/user_list.html"


class UserDetailView(generic.DetailView):
    """User Detail class."""

    model = User
    template_name = "mixtape/user_detail.html"
