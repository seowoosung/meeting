from django.views.generic import FormView, TemplateView
from .forms import PhotoUploadForm
from django.shortcuts import redirect

class ProfileView(TemplateView):
    template_name = "app/profile.html"

class EditView(FormView):
    form_class = PhotoUploadForm
    template_name = "app/edit.html"

    def form_valid(self, form):
        user = self.request.user

        user.photo = form.cleaned_data['photo']
        user.save()

        return redirect('app:profile')


