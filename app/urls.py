from django.urls import path
from app import views
from app.views import ProfileView

urlpatterns = [
    path('', views.signup, name = 'join'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
]
