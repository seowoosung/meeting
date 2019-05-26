from django.views.generic import TemplateView
from accounts.views import GuestOnlyView 

class IndexPageView(GuestOnlyView, TemplateView):
    template_name = 'main/index.html'
