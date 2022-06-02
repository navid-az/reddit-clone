from django.urls import path

from .views import ServerView, ServerFollowView

app_name= 'servers'

urlpatterns = [
    path('<str:server_tag>', ServerView.as_view(), name='server' ),
    path('follow/<str:server_tag>', ServerFollowView.as_view(), name='follow')
]
