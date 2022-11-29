"""views.py."""
from django.shortcuts import redirect, render
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

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class PlaylistDetailView(generic.DetailView):
    """Playlist Detail class."""

    model = Playlist
    template_name = "mixtape/playlist_detail.html"  # file name is lower case

    def get_context_data(self, **kwargs):
        """Check if user owns playlist."""
        context = super().get_context_data(**kwargs)
        context["is_owner"] = self.get_object().creator.user == self.request.user
        # print(context)
        # print(self.get_object().creator)   name
        # print(self.request.user)   email
        return context

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongListView(generic.ListView):
    """Song List class."""

    model = Song
    template_name = "mixtape/song_list.html"  # file name is lower case

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongDetailView(generic.DetailView):
    """Song Detail class."""

    model = Song
    template_name = "mixtape/song_detail.html"  # file name is lower case

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class UserListView(generic.ListView):
    """User List class."""

    model = User
    template_name = "mixtape/user_list.html"

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class UserDetailView(generic.DetailView):
    """User Detail class."""

    model = User
    template_name = "mixtape/user_detail.html"

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongCreateView(generic.CreateView):
    """Song create view."""

    model = Song
    form_class = SongCreateForm
    # template_name = "mixtape/song_create.html"
    template_name = "mixtape/generic_create_update_form.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:song_list")
    extra_context = {"title_text": "Adding a New Song!", "button_text": "Create"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongUpdateView(generic.UpdateView):
    """Song update view."""

    model = Song
    form_class = SongUpdateForm
    template_name = "mixtape/generic_create_update_form.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:song_list")
    extra_context = {"title_text": "Update Song", "button_text": "Update"}


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
    # template_name = "mixtape/playlist_create.html"
    template_name = "mixtape/generic_create_update_form.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:playlist_list")
    extra_context = {"title_text": "Creating a New Playlist", "button_text": "Create"}


class PlaylistUpdateView(generic.UpdateView):
    """Playlist update view."""

    model = Playlist
    form_class = PlaylistUpdateForm
    template_name = "mixtape/generic_create_update_form.html"
    # which page to show upon success

    success_url = reverse_lazy("mixtape:playlist_list")
    extra_context = {"title_text": "Updating Playlist", "button_text": "Update"}


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
    # template_name = "mixtape/user_create.html"
    template_name = "mixtape/generic_create_update_form.html"
    # which page to show upon success
    # replace “home” with one of the names in urls_patterns of urls.py
    success_url = reverse_lazy("mixtape:user_list")
    extra_context = {"title_text": "Creating a New User!", "button_text": "Create"}

    def form_valid(self, form):
        """Validate date."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserUpdateView(generic.UpdateView):
    """User update view."""

    model = User
    form_class = UserUpdateForm
    template_name = "mixtape/generic_create_update_form.html"
    # which page to show upon success
    # replace “home” with one of the names in urls_patterns of urls.py
    success_url = reverse_lazy("mixtape:user_list")
    extra_context = {"title_text": "Updating Existing User!", "button_text": "Update"}


class UserDeleteView(generic.DeleteView):
    """User delete view."""

    model = User
    template_name = "mixtape/user_confirm_delete.html"
    # which page to show upon success
    # replace “home” with one of the names in urls_patterns of urls.py
    success_url = reverse_lazy("mixtape:user_list")
