from django.urls import path
from .views import UserProfileSettingsView, UserProfileView, UserSavedPosts

app_name = 'user'

urlpatterns = [
    path('<str:username>/profile/', UserProfileView.as_view(), name='profile'),
    path('<str:username>/profile/settings', UserProfileSettingsView.as_view(), name='profile-settings'),
    path('<str:username>/saves/', UserSavedPosts.as_view(), name='saved-posts'),
]
