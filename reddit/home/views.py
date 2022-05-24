from xmlrpc.client import Server
from django.shortcuts import render
from django.views import View
from posts.models import Post, Comment
from servers.models import Server

# Create your views here.
class Home(View):
    def get(self, request):
        posts = Post.objects.all()
        servers = Server.objects.all()
        return render(request, 'home/home.html',{'servers':servers, 'posts':posts})

