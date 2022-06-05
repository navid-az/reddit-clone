from django.urls import path
from .views import UserProfileSettingsView, UserProfileView

app_name = 'user'

urlpatterns = [
    path('<str:username>/profile/', UserProfileView.as_view(), name='profile'),
    path('<str:username>/profile/settings', UserProfileSettingsView.as_view(), name='profile-settings')
]
