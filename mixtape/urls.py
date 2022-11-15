"""Urls of mixtape."""
from django.urls import path

import mixtape
from mixtape import views

app_name = "mixtape"
urlpatterns = [
    path("Song", views.SongListView.as_view(), name="song_list"),
    path("Song/<int:pk>/", views.SongDetailView.as_view(), name="song_detail"),

    path("Liked", views.LikedListView.as_view(), name="liked_list"),
    path("Liked/<int:pk>/", views.LikedDetailView.as_view(), name="liked_detail"),

    path("Playlist", views.PlaylistListView.as_view(), name="playlist_list"),
    path("Playlist/<int:pk>/", views.PlaylistDetailView.as_view(), name="playlist_detail"),
]
