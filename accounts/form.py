from django import forms
from django.db import models
from .models import User, User_Profiles


class userlogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

    def __str__(self):
        return self.user.username

