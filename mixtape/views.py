"""views.py."""
from django.shortcuts import render
from django.views import generic
from mixtape.models import Song, Liked

# Create your views here.


class SongListView(generic.ListView):
    """Song List class."""

    model = Song
    template_name = "mixtape/song_list.html"  # file name is lower case


class SongDetailView(generic.DetailView):
    """Song Detail class."""

    model = Song
    template_name = "mixtape/song_detail.html"  # file name is lower case


class LikedListView(generic.ListView):
    """Liked List class."""

    model = Liked
    template_name = "mixtape/liked_list.html"


class LikedDetailView(generic.DetailView):
    """Liked Detail class."""

    model = Liked
    template_name = "mixtape/Liked_detail.html"
