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


class forgotpasswordform(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
    