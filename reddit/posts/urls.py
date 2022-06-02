from django.urls import path
from .views import DeletePostView, PostPageView, UpdatePostView, CreatePostView, CreateReplyView

app_name = 'posts'

urlpatterns = [
    path('<int:post_id>/', PostPageView.as_view(), name='post-page'),
    path('create/<int:pk>', CreatePostView.as_view(), name='create-post'),
    path('reply/<int:post_id>/<int:comment_id>', CreateReplyView.as_view(), name='comment-reply'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
]
