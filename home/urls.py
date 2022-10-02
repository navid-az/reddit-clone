from django.urls import path
from .views import Home, NewPosts, SearchAjaxView, savePostAjaxView

app_name = 'home'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('new/', NewPosts.as_view(), name='new_posts'),
    path('search/', SearchAjaxView, name='search'),
    path('save/', savePostAjaxView, name='save-post'),
]
