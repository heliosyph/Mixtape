"""views.py."""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from mixtape.forms import (PlaylistCreateForm, PlaylistUpdateForm,
                           SongCreateForm, SongUpdateForm, UserCreateForm,
                           UserUpdateForm)
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


class SongCreateView(generic.CreateView):
    """Song create view."""

    model = Song
    form_class = SongCreateForm
    template_name = "mixtape/song_create.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:song_list")


class SongUpdateView(generic.UpdateView):
    """Song update view."""

    model = Song
    form_class = SongUpdateForm
    template_name = "mixtape/song_update.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:song_list")


class SongDeleteView(generic.DeleteView):
    """Song delete view."""

    model = Song
    template_name = "mixtape/song_confirm_delete.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:song_list")


class PlaylistCreateView(generic.CreateView):
    """Playlist create view."""

    model = Playlist
    form_class = PlaylistCreateForm
    template_name = "mixtape/playlist_create.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:playlist_list")


class PlaylistUpdateView(generic.UpdateView):
    """Playlist create view."""

    model = Playlist
    form_class = PlaylistUpdateForm
    template_name = "mixtape/playlist_update.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:playlist_list")


class PlaylistDeleteView(generic.DeleteView):
    """Playlist create view."""

    model = Playlist
    template_name = "mixtape/playlist_confirm_delete.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:playlist_list")


class UserCreateView(generic.CreateView):
    """User create view."""

    model = User
    form_class = UserCreateForm
    template_name = "mixtape/user_create.html"
    # which page to show upon success
    # replace “home” with one of the names in urls_patterns of urls.py
    success_url = reverse_lazy("mixtape:user_list")

    def form_valid(self, form):
        """Validate date."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserUpdateView(generic.UpdateView):
    """User update view."""

    model = User
    form_class = UserUpdateForm
    template_name = "mixtape/user_update.html"
    # which page to show upon success
    # replace “home” with one of the names in urls_patterns of urls.py
    success_url = reverse_lazy("mixtape:user_list")


class UserDeleteView(generic.DeleteView):
    """User create view."""

    model = User
    template_name = "mixtape/user_confirm_delete.html"
    # which page to show upon success
    # replace “home” with one of the names in urls_patterns of urls.py
    success_url = reverse_lazy("mixtape:user_list")
