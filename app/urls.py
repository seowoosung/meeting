from django.urls import path
from app.views import ProfileView

app_name = 'app'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name = 'profile'),
]
