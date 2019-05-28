from django.views.generic import FormView, TemplateView
from django.forms import ValidationError
from .forms import PhotoUploadForm
from django.shortcuts import redirect
import os

class ProfileView(TemplateView):
    template_name = "app/profile.html"

class EditView(FormView):
    form_class = PhotoUploadForm
    template_name = "app/edit.html"

    def form_valid(self, form):
        user = self.request.user

        if 'photo' in form.changed_data:
            if os.path.isfile(user.photo.path):
                os.remove(user.photo.path)
            user.photo = form.cleaned_data['photo']
        
        user.username = form.cleaned_data['username']
        user.save()
    
        return redirect('app:profile')

    def form_invalid(self, form):
        raise ValidationError(form.errors)

