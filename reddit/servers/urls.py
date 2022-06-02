from django.urls import path
from .views import ServerView

app_name= 'servers'

urlpatterns = [
    path('<str:server_tag>', ServerView.as_view(), name='server' )
]
