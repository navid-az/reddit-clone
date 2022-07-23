from django.urls import path
from .views import ServerView, ServerFollowView, CreateServerView, ServerModeratingView

app_name= 'servers'

urlpatterns = [
    path('<str:server_tag>', ServerView.as_view(), name='server' ),
    path('follow/<str:server_tag>', ServerFollowView.as_view(), name='follow'),
    path('create/', CreateServerView.as_view(), name='create'),
    path('moderating-page/', ServerModeratingView.as_view(), name='moderating-page' )
]
