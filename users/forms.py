from users.models import (
    Userprofile,
    Token,
)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from client.models import Clientprofile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Userprofile
        fields = ("username","phoneno")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Userprofile
        exclude = []
class Clientregistrationform(forms.ModelForm):
    class Meta:
        model=Clientprofile
        fields=['height','weight']

