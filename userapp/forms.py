from django import forms
from userapp.models import userdata
from django.contrib.auth.models import User


class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']


class userprofileform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = ['city','state','door_no','street','zipcode','profile_pic']


class updateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class updateprofileform(forms.ModelForm):
    class Meta:
        model = userdata
        fields = ['city','state','door_no','street','zipcode','profile_pic']


