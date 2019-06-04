from django.views.generic import FormView, TemplateView
from django.forms import ValidationError
from .forms import EditForm
from django.shortcuts import redirect
from PIL import Image
import os

class ProfileView(TemplateView):
    template_name = "app/profile.html"

class EditView(FormView):
    form_class = EditForm
    template_name = "app/edit.html"

    def form_valid(self, form):
        user = self.request.user

        if 'photo' in form.changed_data:
            if os.path.isfile(user.photo.path):
                os.remove(user.photo.path)
            user.photo = self.get_cropped_image(form, user)
        
        user.username = form.cleaned_data['username']
        user.age = form.cleaned_data['age']
        user.introduction = form.cleaned_data['introduction']
        user.is_male = form.cleaned_data['is_male']
        user.save()
    
        return redirect('app:profile')

    def form_invalid(self, form):
        raise ValidationError(form.errors)

    def get_cropped_image(self, form, user):
        x1 = form.cleaned_data.get('top_left_x')
        y1 = form.cleaned_data.get('top_left_y')
        x2 = form.cleaned_data.get('bottom_right_x')
        y2 = form.cleaned_data.get('bottom_right_y')

        image = Image.open(form.cleaned_data['photo'])
        cropped_image = image.crop((x1, y1, x2, y2))
        cropped_image.save(user.photo.path ,'PNG')

        return user.photo