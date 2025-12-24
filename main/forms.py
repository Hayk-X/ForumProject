from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegister(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=300)

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=2000)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']