from django.shortcuts import redirect, render
from django.views import View
from .models import Server, ServerFollow
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ServerView(LoginRequiredMixin,View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        posts = server.posts.all()
        is_following = False
        relation = ServerFollow.objects.filter(server=server, user=request.user)
        if relation.exists():
            is_following = True
        return render(request, 'servers/server.html', {'server':server, 'posts':posts, 'is_following':is_following})

class ServerFollowView(View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        relation = ServerFollow.objects.filter(server=server, user=request.user)
        if relation.exists():
            relation.delete()
        else:
            ServerFollow(server=server, user=request.user).save()
        return redirect('servers:server' ,server.tag )