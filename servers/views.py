from email import message
from http import server
from django.shortcuts import redirect, render
from django.views import View
from .models import Server, ServerFollow, ServerModeratorPermission, ServerPostTag, ServerRule, ServerUserTag, ServerModerator
from .forms import CreateServerForm, CreatePostTagForm, CreateUserTagForm, CreateRuleForm, UpdateModeratorPermissionsForm
from posts.models import Vote
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q

import itertools
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
            saved_form.name = saved_form.tag.capitalize()
            saved_form.save()
            return render(request, 'servers/create-server.html')
        messages.error(request, 'This is wrong')
        return render(request, 'servers/create-server.html', {'create_form':create_form})


class ServerModeratingView(LoginRequiredMixin, View):
    def get(self, request, server_tag):        
        server = Server.objects.get(tag=server_tag)
        # server_post_tags = server.post_tags.all()
        # , "server_post_tags":server_post_tags
        moderator = ServerModerator.objects.filter(user=request.user, server=server)
        if moderator.exists():
            return render(request, 'servers/moderating-page.html', {"server":server})
        messages.warning(request, 'شما مدیر این سرور نیستید')
        return redirect('home:home')
class TagsAndFlairsView(LoginRequiredMixin, View):
    form_class = CreatePostTagForm
    form_class_2 = CreateUserTagForm

    def get(self, request, server_tag):
        create_post_tag_form = self.form_class(prefix='post-tag')
        create_user_tag_form = self.form_class_2(prefix='user-tag')

        server = Server.objects.get(tag=server_tag)
        moderator = ServerModerator.objects.filter(user=request.user, server=server)

        server_post_tags = server.post_tags.all()
        server_user_tags = server.user_tags.all()
        if moderator.exists():
            return render(request, 'servers/tags-flairs.html', {"server":server, "server_post_tags":server_post_tags, "server_user_tags":server_user_tags, "create_post_tag_form":create_post_tag_form, "create_user_tag_form":create_user_tag_form})
        messages.warning(request, 'شما مدیر این سرور نیستید')
        return redirect('home:home')

    def post(self, request, server_tag):
        create_post_tag_form = self.form_class(request.POST, prefix='post-tag')
        create_user_tag_form = self.form_class_2(request.POST, prefix='user-tag')

        server = Server.objects.get(tag=server_tag)
        moderator = ServerModerator.objects.get(user=request.user, server=server)
        permission = ServerModeratorPermission.objects.filter(moderator=moderator, server=server, allow_create_tag=True)
        if permission.exists():
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
        messages.error(request, 'شما نمیتوانید تگ ایجاد کنید')
        return redirect('servers:server-tags-and-flairs', server_tag)
class DeleteTagsAndFlairsView(LoginRequiredMixin ,View):
    def get(self, request, *args, **kwargs):
        post_tag = ServerPostTag.objects.filter(pk=kwargs['tag_id'], creator=request.user)
        user_tag = ServerUserTag.objects.filter(pk=kwargs['tag_id'], creator=request.user)

        server = Server.objects.get(tag=kwargs['server_tag'])
        moderator = ServerModerator.objects.get(user=request.user, server=server)
        permission = ServerModeratorPermission.objects.filter(moderator=moderator, server=server, allow_delete_tag=True)
        if permission.exists():
            if post_tag.exists():
                post_tag.delete()
                return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
            elif user_tag.exists():
                user_tag.delete()
                return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
            else:
                messages.error(request, 'فقط مدیر سرور میتواند این تگ را حذف کند')
                return redirect('home:home')
        messages.error(request, 'شما اجازه حذف تگ در این سرور را ندارید')
        return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
class RulesView(LoginRequiredMixin, View):
    class_form = CreateRuleForm

    def get(self, request, *args, **kwargs):
        create_rule_form = self.class_form()

        server = Server.objects.get(tag=kwargs['server_tag'])
        server_rules = server.rules.all()
        moderator = ServerModerator.objects.filter(user=request.user, server=server)
        if moderator.exists():
            return render(request, 'servers/rules.html', {"server":server, "server_rules":server_rules, "create_rule_form":create_rule_form})
        messages.warning(request, 'شما مدیر این سرور نیستید')
        return redirect('home:home')

    def post(self, request, *args, **kwargs):
        create_rule_form = self.class_form(request.POST)

        server = Server.objects.get(tag=kwargs['server_tag'])
        server_rules = server.rules.all()

        moderator = ServerModerator.objects.get(user=request.user, server=server)
        permission = ServerModeratorPermission.objects.filter(moderator=moderator, server=server, allow_create_rule=True)
        if permission.exists():
            if create_rule_form.is_valid():
                new_rule = create_rule_form.save(commit=False)
                new_rule.server = server
                new_rule.creator = request.user
                new_rule.save()
                return redirect('servers:server-rules', kwargs['server_tag'])
            return render(request, 'servers/rules.html', {"server":server, "server_rules":server_rules, "create_rule_form":create_rule_form})
        messages.error(request, 'شما نمیتوانید قانون ایجاد کنید')
        return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])

class DeleteRulesView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        server = Server.objects.get(tag=kwargs['server_tag'])
        moderator = ServerModerator.objects.get(user=request.user, server=server)
        permission = ServerModeratorPermission.objects.filter(moderator=moderator, server=server, allow_delete_rule=True)
        if permission.exists():
            rule = ServerRule.objects.filter(pk=kwargs['rule_id'], creator=request.user)
            if rule.exists():
                rule.delete()
                return redirect('servers:server-rules', kwargs['server_tag'])
            else:
                messages.error(request, 'فقط مدیر سرور میتواند قانون سرور را حذف کند')
                return redirect('home:home')
        messages.error(request, 'شما اجازه حذف قانون در این سرور را ندارید')
        return redirect('servers:server-tags-and-flairs', kwargs['server_tag'])
class ModeratorSettingsView(View):
    def get(self, request, *args, **kwargs):
        server = Server.objects.get(tag=kwargs['server_tag'])
        moderators = server.moderator_of.all()
        return render(request, 'servers/moderator-settings.html', {'moderators':moderators, 'server':server})

class ModeratorPermissionsView(View):
    form_class = UpdateModeratorPermissionsForm

    def get(self, request, *args, **kwargs):
        server = Server.objects.get(tag=kwargs['server_tag'])
        moderator = server.moderator_of.get(user=kwargs['user_id'])
        permission = server.permissions.get(moderator=moderator)
        form = self.form_class(instance=permission)
        return render(request, 'servers/moderator-permissions.html', {'server':server, 'moderator':moderator, 'form':form})
    
    def post(self, request, *args, **kwargs):
        server = Server.objects.get(tag=kwargs['server_tag'])
        moderator = server.moderator_of.get(user=kwargs['user_id'])
        permission = server.permissions.get(moderator=moderator)
        form = self.form_class(request.POST, instance=permission)
        if form.is_valid():
            updated_permission = form.save(commit=False)
            updated_permission.server = server
            updated_permission.moderator = moderator
            moderators = server.moderator_of.all()
            updated_permission.save()
            messages.success(request, 'yes')
            return render(request, 'servers/moderator-settings.html', {'moderators':moderators, 'server':server})
        messages.success(request, 'yes')
        return redirect(request, 'servers:server-moderator-settings', kwargs['server_tag'])
    

class UserSettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'servers/user-settings.html')
 
class ChooseServerAjaxView(View):
    def get(self, request):
        moderator = ServerModerator.objects.get(user=request.user)
        # servers = Server.objects.filter(creator=request.user)
        moderator_servers = moderator.server.all()
        user_servers = itertools.chain(moderator_servers)
        data = []
        for i in user_servers:
            list ={
            'tag':i.tag,
            'name':i.name,
            'about':i.about,
            'server_type':i.server_type
            }
            data.append(list)
        return JsonResponse({'data':data})