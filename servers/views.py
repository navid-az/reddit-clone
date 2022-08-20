from django.shortcuts import redirect, render
from django.views import View
from .models import Server, ServerFollow, ServerPostTag, ServerRule, ServerUserTag, ServerModerator
from .forms import CreateServerForm, CreatePostTagForm, CreateUserTagForm, CreateRuleForm
from posts.models import Vote
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class ServerView(View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        posts = server.posts.all()
        post_tags = server.post_tags.all()
        user_tags = server.user_tags.all()
        if user_tags.filter(user=request.user).exists():
            current_user_tag = user_tags.get(user=request.user)
        else:
            current_user_tag = None
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
        return render(request, 'servers/server.html', {'server':server, 'posts':posts, 'is_following':is_following, 'vote_count':vote_count, 'user_tags':user_tags, 'current_user_tag':current_user_tag, 'post_tags':post_tags})

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
        messages.error(request, 'This is wrong')
        return render(request, 'servers/create-server.html', {'create_form':create_form})


class ServerModeratingView(LoginRequiredMixin, View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag, creator=request.user)
        server_post_tags = server.post_tags.all()
        return render(request, 'servers/moderating-page.html', {"server":server, "server_post_tags":server_post_tags})
class TagsAndFlairsView(LoginRequiredMixin, View):
    form_class = CreatePostTagForm
    form_class_2 = CreateUserTagForm

    def get(self, request, server_tag):
        create_post_tag_form = self.form_class(prefix='post-tag')
        create_user_tag_form = self.form_class_2(prefix='user-tag')
        
        server = Server.objects.get(tag=server_tag, creator=request.user)
        server_post_tags = server.post_tags.all()
        server_user_tags = server.user_tags.all()
        return render(request, 'servers/tags-flairs.html', {"server":server, "server_post_tags":server_post_tags, "server_user_tags":server_user_tags, "create_post_tag_form":create_post_tag_form, "create_user_tag_form":create_user_tag_form})

    def post(self, request, server_tag):
        create_post_tag_form = self.form_class(request.POST, prefix='post-tag')
        create_user_tag_form = self.form_class_2(request.POST, prefix='user-tag')

        server = Server.objects.get(tag=server_tag, creator=request.user)
        if create_post_tag_form.is_valid():
            created_post_tag = create_post_tag_form.save(commit=False)
            created_post_tag.server = server
            created_post_tag.creator = request.user
            created_post_tag.save()
            return redirect('servers:server-tags-and-flairs', server_tag)
        elif create_user_tag_form.is_valid():
            created_user_tag = create_user_tag_form.save(commit=False)
            created_user_tag.server = server
            created_user_tag.creator = request.user
            created_user_tag.save()
            return redirect('servers:server-tags-and-flairs', server_tag)
        return render(request, 'servers/tags-flairs.html', {"server":server, "create_post_tag_form":create_post_tag_form, "create_user_tag_form":create_user_tag_form})

class DeleteTagsAndFlairsView(LoginRequiredMixin ,View):
    def get(self, request, *args, **kwargs):
        post_tag = ServerPostTag.objects.filter(pk=kwargs['tag_id'], creator=request.user)
        user_tag = ServerUserTag.objects.filter(pk=kwargs['tag_id'], creator=request.user)
        if post_tag.exists():
            post_tag.delete()
            return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
        elif user_tag.exists():
            user_tag.delete()
            return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
        else:
            messages.error(request, 'فقط مدیر سرور میتواند این تگ را حذف کند')
            return redirect('home:home')
class RulesView(LoginRequiredMixin, View):
    class_form = CreateRuleForm

    def get(self, request, server_tag):
        create_rule_form = self.class_form()

        server = Server.objects.get(tag=server_tag, creator=request.user)
        server_rules = server.rules.all()
        return render(request, 'servers/rules.html', {"server":server, "server_rules":server_rules, "create_rule_form":create_rule_form})

    def post(self, request, server_tag):
        create_rule_form = self.class_form(request.POST)

        server = Server.objects.get(tag=server_tag, creator=request.user)
        server_rules = server.rules.all()
        if create_rule_form.is_valid():
            new_rule = create_rule_form.save(commit=False)
            new_rule.server = server
            new_rule.creator = request.user
            new_rule.save()
            return redirect('servers:server-rules', server_tag)
        return render(request, 'servers/rules.html', {"server":server, "server_rules":server_rules, "create_rule_form":create_rule_form})

class DeleteRulesView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        rule = ServerRule.objects.filter(pk=kwargs['rule_id'], creator=request.user)
        if rule.exists():
            rule.delete()
            return redirect('servers:server-rules', kwargs['server_tag'])
        else:
            messages.error(request, 'فقط مدیر سرور میتواند قانون سرور را حذف کند')
            return redirect('home:home')


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

class ModeratorSettingsView(View):
    def get(self, request, *args, **kwargs):
        server = Server.objects.get(tag=kwargs['server_tag'])
        moderators = ServerModerator.objects.filter(server=server)
        return render(request, 'servers/moderator-settings.html', {'moderators':moderators, 'server':server})