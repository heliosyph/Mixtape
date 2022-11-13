"""views.py."""
from django.shortcuts import render
from django.views import generic
from mixtape.models import Song

# Create your views here.


class SongListView(generic.ListView):
    model = Song
    template_name = "mixtape/song_list.html"  # file name is lower case


class SongDetailView(generic.DetailView):
    model = Song
    template_name = "mixtape/song_detail.html"  # file name is lower case
