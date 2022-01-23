from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class studentregisterform(UserCreationForm):
    email=forms.EmailField()
    grade=forms.CharField(max_length=20)
    class meta:
        model=User
        field=['username','email','password1','password2','grade']