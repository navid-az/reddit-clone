from django.urls import path
from .views import (DeletePostView, PostPageView, UpdatePostView, CreatePostView,
 CreateReplyView, CreatePostAjaxView, votePostAjaxView, savePostAjaxView)

app_name = 'posts'

urlpatterns = [
    path('<int:post_id>/', PostPageView.as_view(), name='post-page'),
    path('create/<int:pk>', CreatePostView.as_view(), name='create-post'),
    path('create/r/<str:server_tag>/info', CreatePostAjaxView.as_view(), name='server-info'),
    path('reply/<int:post_id>/<int:comment_id>', CreateReplyView.as_view(), name='comment-reply'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
    path('save/', savePostAjaxView, name='save-post'),
    path('vote/', votePostAjaxView, name='vote-post')
]
