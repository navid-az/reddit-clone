from django.shortcuts import redirect, render
from django.views import View
from .models import Server, ServerFollow
from .forms import CreateServerForm
from posts.models import Vote
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
class ServerView(View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        posts = server.posts.all()
        upvote = Vote.objects.filter(choice='up').count()
        downvote = Vote.objects.filter(choice='down').count()
        vote_count = upvote - downvote
        is_following = False
        # the code bellow will make sure to show this page to all users even to those whom haven't logged in yet
        qs = ServerFollow.objects.filter(server=server)
        if qs and request.user.is_authenticated:
            qs = qs.filter(user=request.user)
            if qs.exists():
                is_following = True
        return render(request, 'servers/server.html', {'server':server, 'posts':posts, 'is_following':is_following, 'vote_count':vote_count})
class ServerFollowView(LoginRequiredMixin, View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        relation = ServerFollow.objects.filter(server=server, user=request.user)
        if relation.exists():
            relation.delete()
        else:
            ServerFollow(server=server, user=request.user).save()
        return redirect('servers:server', server.tag)

class CreateServerView(LoginRequiredMixin, View):
    form_class = CreateServerForm

    def post(self, request):
        create_form = self.form_class(request.POST)
        if create_form.is_valid():
            saved_form = create_form.save(commit=False)
            saved_form.creator = request.user
            saved_form.save()
            return render(request, 'servers/create-server.html')
        messages.error(request, 'wtf')
        return render(request, 'servers/create-server.html', {'create_form':create_form})


class ServerModeratingView(LoginRequiredMixin, View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag, creator=request.user)
        server_tags = server.tags.all()
        return render(request, 'servers/moderating-page.html', {"server":server, "server_tags":server_tags})
class TagsAndFlairsView(LoginRequiredMixin, View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag, creator=request.user)
        server_tags = server.tags.all()
        return render(request, 'servers/tags-flairs.html', {"server":server, "server_tags":server_tags})

class RulesView(LoginRequiredMixin, View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag, creator=request.user)
        server_tags = server.tags.all()
        return render(request, 'servers/rules.html', {"server":server, "server_tags":server_tags})

class ModeratorSettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'servers/moderator-settings.html')
        
class UserSettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'servers/user-settings.html')
 
class ChooseServerAjaxView(View):
    def get(self, request):
        servers = Server.objects.filter(creator=request.user)
        data = []
        for i in servers:
            item ={
            'tag':i.tag,
            'name':i.name,
            'about':i.about,
            'server_type':i.server_type
            }
            data.append(item)
        return JsonResponse({'data':data})