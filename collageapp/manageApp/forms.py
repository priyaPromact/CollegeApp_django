from django import forms
from manageApp.models import collegeAppUser
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = collegeAppUser
        fields = ('username', 'oAuthID', 'password')