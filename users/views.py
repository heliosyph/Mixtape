"""Accounts view."""
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from users.forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    """User registration view.

    Arguments:
    ---------
    generic : object
        Django generic `CreateView`.

    """

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mixtape:User_create")
    template_name = "registration/signup.html"

    def form_valid(self, form: object) -> object:
        """When the registration form is valid, authenticate and login the user."""
        form_data = form.save()
        login(self.request, form_data)
        return redirect("mixtape:User_create")
