from django.urls import path
from .views import Home, NewPosts

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('new/', NewPosts.as_view(), name='new_posts'),
]
