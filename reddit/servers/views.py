from django.shortcuts import render
from django.views import View
from .models import Server

# Create your views here.
class ServerView(View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        posts = server.posts.all()
        return render(request, 'servers/server.html', {'server':server, 'posts':posts})