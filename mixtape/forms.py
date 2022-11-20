"""Forms for mixtape app."""
from django.forms import ModelForm

from mixtape.models import Playlist, Song, User


class SongCreateForm(ModelForm):
    """Song creation form."""

    class Meta:
        """Meta class."""

        model = Song
        # list of fields to be used in the form
        fields = (
            "song_name",
            "song_length",
            "artist_name",
            "album",
            "song_genre",
            "likes",
            "isFavoriteSong",
        )


class SongUpdateForm(ModelForm):
    """Song creation form."""

    class Meta:
        """Meta class."""

        model = Song
        # list of fields to be used in the form
        fields = (
            "song_name",
            "song_length",
            "artist_name",
            "album",
            "song_genre",
            "likes",
            "isFavoriteSong",
        )


class PlaylistCreateForm(ModelForm):
    """Playlist creation form."""

    class Meta:
        """Meta class."""

        model = Playlist
        # list of fields to be used in the form
        fields = (
            "playlist_name",
            "creator",
            "likes",
            "songs",
            "isPrivate",
            "playlist_description",
        )


class PlaylistUpdateForm(ModelForm):
    """Playlist creation form."""

    class Meta:
        """Meta class."""

        model = Playlist
        # list of fields to be used in the form
        fields = (
            "playlist_name",
            "creator",
            "likes",
            "songs",
            "isPrivate",
            "playlist_description",
        )


class UserCreateForm(ModelForm):
    """User creation form."""

    class Meta:
        """Meta class."""

        model = User
        # list of fields to be used in the form
        fields = (
            "username_creator",
            "isFriend",
            "friend_name",
            "favorite_genre",
            "favorite_artist",
            "status",
        )


class UserUpdateForm(ModelForm):
    """User update form."""

    class Meta:
        """Meta class."""

        model = User
        # list of fields to be used in the form
        fields = (
            "username_creator",
            "isFriend",
            "friend_name",
            "favorite_genre",
            "favorite_artist",
            "status",
        )
