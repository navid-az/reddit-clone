from django.urls import path
from .views import UserProfileView

app_name = 'user'

urlpatterns = [
    path('<str:pk>/profile/', UserProfileView.as_view(), name='profile')
]
