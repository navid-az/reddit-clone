from django.urls import path
from .views import (ServerView, ServerFollowView, CreateServerView, ServerInsightsView, ServerDeleteReportView, TagsAndFlairsView, DeleteTagsAndFlairsView, 
RulesView, DeleteRulesView, LimitationDoneAjaxView, ChooseServerAjaxView, ModeratorSearchAjaxView, ModeratorSettingsView, ModeratorPermissionsView, ServerSettingsView)

app_name= 'servers'

urlpatterns = [
    # server
    path('<str:server_tag>', ServerView.as_view(), name='server'),
    path('follow/<str:server_tag>', ServerFollowView.as_view(), name='server-follow'),
    path('create/', CreateServerView.as_view(), name='server-create'),
    
    # insights
    path('<str:server_tag>/moderating-page/insights/', ServerInsightsView.as_view(), name='server-insights'),
    path('<str:server_tag>/moderating-page/insights/delete-report/<int:report_id>', ServerDeleteReportView.as_view(), name='server-delete-report'),
    
    path('limitation-done/', LimitationDoneAjaxView.as_view(), name='limitation-done'),
    path('moderating-page/', ChooseServerAjaxView.as_view(), name='server-choose'),
    path('get-moderators/', ModeratorSearchAjaxView, name='moderator-search'),

    #tags/flairs
    path('<str:server_tag>/moderating-page/tags-and-flairs', TagsAndFlairsView.as_view(), name='server-tags-and-flairs'),
    path('<str:server_tag>/moderating-page/tags-and-flairs/<int:tag_id>/delete', DeleteTagsAndFlairsView.as_view(), name='server-tag-delete'),

    #rules
    path('<str:server_tag>/moderating-page/rules', RulesView.as_view(), name='server-rules'),
    path('<str:server_tag>/moderating-page/rules/<int:rule_id>/delete', DeleteRulesView.as_view(), name='server-rules-delete'),

    #moderators settings
    path('<str:server_tag>/moderating-page/moderator-settings', ModeratorSettingsView.as_view(), name='server-moderator-settings'),
    path('<str:server_tag>/moderating-page/moderator-settings/<int:user_id>/permissions', ModeratorPermissionsView.as_view(), name='server-moderator-permissions'),

    #server settings
    path('<str:server_tag>/moderating-page/server-settings', ServerSettingsView.as_view(), name='server-settings')
]
