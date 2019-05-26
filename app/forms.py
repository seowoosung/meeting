from PIL import Image
from django import forms
from django.forms import ModelForm
from accounts.models import User


class PhotoUploadForm(ModelForm):
    class Meta:
        model = User
        fields = ['photo']