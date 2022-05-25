from django.urls import path
from .views import DeletePostView, PostPageView, UpdatePostView, CreatePostView, post_tab

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', PostPageView.as_view(), name='post-page'),
    path('create/<int:pk>', CreatePostView.as_view(), name='create-post'),
    path('post-tab/', post_tab, name='post-tab'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),
]
