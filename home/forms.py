

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import Book

class studentregisterform(UserCreationForm):
    email=forms.EmailField()
    grade=forms.CharField(max_length=20)
    class Meta:
        model=User
        fields=['username','email','password1','password2','grade']

class Book_Entry_Form(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'