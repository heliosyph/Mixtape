"""Tests for `users` app."""
from http import HTTPStatus

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase
from django.urls import reverse
from parameterized import parameterized

from mixtape.models import Playlist, Song, User
