from django import forms

class SignUpForm(forms.Form):
    userName = forms.CharField(label='User Name', max_length=30)
    Id = forms.CharField(label='ID', max_length=30)
    password = forms.CharField(label='Password', max_length=30)
