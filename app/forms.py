from PIL import Image
from django import forms
from django.forms import ModelForm
from accounts.models import User


class PhotoUploadForm(ModelForm):
    class Meta:
        model = User
        fields = ['photo', 'username']
        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'item-img file center-block',
                'id' : 'input-photo',
                }),
            'username': forms.TextInput(attrs={
                'id': 'input-username',
                }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False
