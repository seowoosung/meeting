from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = "app/profile.html"