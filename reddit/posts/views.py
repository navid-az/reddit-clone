from django.shortcuts import render
from django.views import View
from .models import Post, Comment

# Create your views here.

class PostPage(View):
    def get(self, request, pk):
        post = Post.objects.get(id = pk)
        comments_count = len(Comment.objects.filter(post = post))
        return render(request, 'posts/post.html',{'post':post,'comments_count':comments_count})
        
