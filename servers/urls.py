from django.urls import path
from .views import (ServerView, ServerFollowView, CreateServerView, ServerModeratingView, TagsAndFlairsView, DeleteTagsAndFlairsView, 
RulesView, DeleteRulesView, ChooseServerAjaxView, ModeratorSettingsView, ModeratorPermissionsView)

app_name= 'servers'

urlpatterns = [
    path('<str:server_tag>', ServerView.as_view(), name='server'),
    path('follow/<str:server_tag>', ServerFollowView.as_view(), name='server-follow'),
    path('create/', CreateServerView.as_view(), name='server-create'),
    
    path('<str:server_tag>/moderating-page/', ServerModeratingView.as_view(), name='server-moderating-page'),
    path('moderating-page/', ChooseServerAjaxView.as_view(), name='server-choose'),
    path('<str:server_tag>/moderating-page/tags-and-flairs', TagsAndFlairsView.as_view(), name='server-tags-and-flairs'),
    path('<str:server_tag>/moderating-page/tags-and-flairs/<int:tag_id>/delete', DeleteTagsAndFlairsView.as_view(), name='server-tag-delete'),

    path('<str:server_tag>/moderating-page/rules', RulesView.as_view(), name='server-rules'),
    path('<str:server_tag>/moderating-page/rules/<int:rule_id>/delete', DeleteRulesView.as_view(), name='server-rules-delete'),

    path('<str:server_tag>/moderating-page/moderator-settings', ModeratorSettingsView.as_view(), name='server-moderator-settings'),
    path('<str:server_tag>/moderating-page/moderator-settings/<int:user_id>/permissions', ModeratorPermissionsView.as_view(), name='server-moderator-permissions'),
    path('moderating-page/user-settings', RulesView.as_view(), name='server-user-settings'),
]
