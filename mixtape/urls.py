"""Urls of mixtape."""
from django.urls import path

import mixtape
from mixtape import views

app_name = "mixtape"
urlpatterns = [
    path("Song", views.SongListView.as_view(), name="song_list"),
    path("Song/<int:pk>/", views.SongDetailView.as_view(), name="song_detail"),
]
