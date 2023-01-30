from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=True, help_text="Required. 30 characters or fewer."
    )
    last_name = forms.CharField(
        max_length=30, required=True, help_text="Required. 30 characters or fewer."
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
        help_text="Required. Inform a valid email address.",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
