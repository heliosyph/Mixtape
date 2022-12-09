"""views.py."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from mixtape import forms
from mixtape.models import Playlist, Song, User


class PlaylistListView(LoginRequiredMixin, generic.ListView):
    """Playlist List class."""

    model = Playlist
    template_name = "mixtape/playlist_list.html"  # file name is lower case

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class PlaylistDetailView(LoginRequiredMixin, generic.DetailView):
    """Playlist Detail class."""

    model = Playlist
    template_name = "mixtape/playlist_detail.html"  # file name is lower case

    def get_context_data(self, **kwargs):
        """Check if user owns playlist."""
        context = super().get_context_data(**kwargs)
        context["is_owner"] = self.get_object().creator.user == self.request.user
        return context

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongListView(LoginRequiredMixin, generic.ListView):
    """Song List class."""

    model = Song
    template_name = "mixtape/song_list.html"  # file name is lower case

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongDetailView(LoginRequiredMixin, generic.DetailView):
    """Song Detail class."""

    model = Song
    template_name = "mixtape/song_detail.html"  # file name is lower case

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class UserListView(LoginRequiredMixin, generic.ListView):
    """User List class."""

    model = User
    template_name = "mixtape/user_list.html"

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    """User Detail class."""

    model = User
    template_name = "mixtape/user_detail.html"

    def get_context_data(self, **kwargs):
        """Check if user owns profile."""
        context = super().get_context_data(**kwargs)
        print(self.get_object().user)
        print(self.request.user)
        context["is_user"] = self.get_object().user == self.request.user
        return context

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongCreateView(LoginRequiredMixin, generic.CreateView):
    """Song create view."""

    model = Song
    form_class = forms.SongCreateForm
    template_name = "mixtape/generic_create_update_form.html"
    success_url = reverse_lazy("mixtape:song_list")
    extra_context = {"title_text": "Adding a New Song!", "button_text": "Create"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class SongUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Song update view."""

    model = Song
    form_class = forms.SongUpdateForm
    template_name = "mixtape/generic_create_update_form.html"
    success_url = reverse_lazy("mixtape:song_list")
    extra_context = {"title_text": "Update Song", "button_text": "Update"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not a super user, return to home page."""
        if not self.request.user.is_superuser:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class SongDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Song delete view."""

    model = Song
    template_name = "mixtape/song_confirm_delete.html"
    success_url = reverse_lazy("mixtape:song_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not a super user, return to home page."""
        if not self.request.user.is_superuser:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class PlaylistCreateView(LoginRequiredMixin, generic.CreateView):
    """Playlist create view."""

    model = Playlist
    form_class = forms.PlaylistCreateForm
    template_name = "mixtape/generic_create_update_form.html"
    success_url = reverse_lazy("mixtape:playlist_list")
    extra_context = {"title_text": "Creating a New Playlist", "button_text": "Create"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not logged in, redirect to sign in page."""
        if not self.request.user.is_authenticated:
            return redirect("login")
        return super().get(request, *args, **kwargs)


class PlaylistUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Playlist update view."""

    model = Playlist
    form_class = forms.PlaylistUpdateForm
    template_name = "mixtape/generic_create_update_form.html"
    success_url = reverse_lazy("mixtape:playlist_list")
    extra_context = {"title_text": "Updating Playlist", "button_text": "Update"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect; Otherwise, show details."""
        if self.get_object().creator.user != self.request.user:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class PlaylistDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Playlist create view."""

    model = Playlist
    template_name = "mixtape/playlist_confirm_delete.html"
    success_url = reverse_lazy("mixtape:playlist_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect; Otherwise, show details."""
        if self.get_object().creator.user != self.request.user:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class UserCreateView(LoginRequiredMixin, generic.CreateView):
    """User create view."""

    model = User
    form_class = forms.UserCreateForm
    template_name = "mixtape/generic_create_update_form.html"
    success_url = reverse_lazy("mixtape:user_list")
    extra_context = {"title_text": "Creating a New User!", "button_text": "Create"}

    def form_valid(self, form):
        """Validate date."""
        print(self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    """User update view."""

    model = User
    form_class = forms.UserUpdateForm
    template_name = "mixtape/generic_create_update_form.html"
    success_url = reverse_lazy("mixtape:user_list")
    extra_context = {"title_text": "Updating Existing User!", "button_text": "Update"}

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect; Otherwise, show details."""
        if self.get_object().user != self.request.user:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    """User delete view."""

    model = User
    template_name = "mixtape/user_confirm_delete.html"
    success_url = reverse_lazy("mixtape:user_list")

    def get(self, request: object, *args, **kwargs) -> object:
        """If user is not the owner of the object, redirect; Otherwise, show details."""
        if self.get_object().user != self.request.user:
            return redirect("home")
        return super().get(request, *args, **kwargs)
