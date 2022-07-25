from django.urls import path
from .views import ServerView, ServerFollowView, CreateServerView, ServerModeratingView, TagsAndFlairsView, RulesView

app_name= 'servers'

urlpatterns = [
    path('<str:server_tag>', ServerView.as_view(), name='server'),
    path('follow/<str:server_tag>', ServerFollowView.as_view(), name='server-follow'),
    path('create/', CreateServerView.as_view(), name='server-create'),
    path('moderating-page/', ServerModeratingView.as_view(), name='server-moderating-page'),
    path('moderating-page/tags-and-flairs', TagsAndFlairsView.as_view(), name='server-tags-and-flairs'),
    path('moderating-page/rules', RulesView.as_view(), name='server-rules'),
    path('moderating-page/moderator-settings', RulesView.as_view(), name='server-moderator-settings'),
    path('moderating-page/user-settings', RulesView.as_view(), name='server-user-settings'),
]
