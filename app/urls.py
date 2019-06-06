from django.urls import path
from app.views import ProfileView, EditView, CandidateListView

app_name = 'app'

urlpatterns = [
    path('', ProfileView.as_view()),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('profile/edit', EditView.as_view(), name = 'edit'),
    path('list/', CandidateListView.as_view(), name = 'list'),
]
