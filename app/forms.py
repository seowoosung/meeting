from django import forms
from django.forms import ModelForm
from accounts.models import User

TRUE_FALSE_CHOICES = (
    (True, 'male'),
    (False, 'female')
)

class EditForm(ModelForm):
    top_left_x = forms.FloatField(widget=forms.HiddenInput())
    top_left_y = forms.FloatField(widget=forms.HiddenInput())
    bottom_right_x = forms.FloatField(widget=forms.HiddenInput())
    bottom_right_y = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['photo', 'username', 'age', 'introduction', 'is_male', 'top_left_x', 'top_left_y', 'bottom_right_x', 'bottom_right_y']
        widgets = {
            'is_male': forms.Select(choices=TRUE_FALSE_CHOICES),
            'photo': forms.FileInput(attrs={
            'class': 'item-img file center-block',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False
        self.fields['top_left_x'].required = False
        self.fields['top_left_y'].required = False
        self.fields['bottom_right_x'].required = False
        self.fields['bottom_right_y'].required = False
        self.fields['username'].widget.attrs.update({
            'class': 'form-field'
            })
        self.fields['age'].widget.attrs.update({
            'class': 'form-field'
            })
        self.fields['introduction'].widget.attrs.update({
            'class': 'form-field'
            })