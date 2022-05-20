from django.urls import path
from .views import PostPage

app_name = 'posts'

urlpatterns = [
    path('<str:pk>/', PostPage.as_view(), name='post-page'),
]
