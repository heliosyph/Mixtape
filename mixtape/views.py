"""views.py."""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mixtape.models import Playlist, Song, User
from mixtape.forms import SongCreateForm, SongUpdateForm


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


class SongCreateView(generic.CreateView):
    """Song create view."""

    model = Song
    form_class = SongCreateForm
    template_name = "mixtape/song_create.html"
    # which page to show upon success

    success_url = reverse_lazy("Song")


class SongUpdateView(generic.UpdateView):
    """Song update view."""

    model = Song
    form_class = SongUpdateForm
    template_name = "mixtape/song_update.html"
    # which page to show upon success

    success_url = reverse_lazy("Song")


class SongDeleteView(generic.DeleteView):
    """Song delete view."""

    model = Song
    template_name = "mixtape/song_confirm_delete.html"
    # which page to show upon success

    success_url = reverse_lazy("Song")
