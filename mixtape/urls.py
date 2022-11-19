"""Urls of mixtape."""
from django.urls import path

import mixtape
from mixtape import views

app_name = "mixtape"
urlpatterns = [
    path("Song", views.SongListView.as_view(), name="song_list"),
    path("Song/<int:pk>/", views.SongDetailView.as_view(), name="song_detail"),
    path("Playlist", views.PlaylistListView.as_view(), name="playlist_list"),
    path("Playlist/<int:pk>/", views.PlaylistDetailView.as_view(), name="playlist_detail"),
    path("User", views.UserListView.as_view(), name="user_list"),
    path("User/<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
]
