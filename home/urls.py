from django.urls import path
from .views import Home, NewPosts, SearchAjaxView, HotPosts

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('new/', NewPosts.as_view(), name='new_posts'),
    path('hot/', HotPosts.as_view(), name='hot_posts'),
    path('search/', SearchAjaxView, name='search'),
]
