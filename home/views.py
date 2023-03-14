from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from posts.models import Post, PostSave
from servers.models import Server
from django.contrib.auth.models import User
import itertools
from django.db.models import F


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class Home(View):
    def get(self, request):
        servers = Server.objects.all()
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user_following_servers = user.following_server.values('server')
            posts = Post.objects.filter(server__in=user_following_servers)
        else:
            posts = Post.objects.all()
        return render(request, 'home/home.html',{'servers':servers, 'posts':posts})
            
class NewPosts(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user_following_servers = user.following_server.values('server')
            posts = Post.objects.filter(server__in=user_following_servers).order_by('-created')
        else:
            posts = Post.objects.order_by('-created')
        return render(request, 'home/new.html', {'posts':posts})

class HotPosts(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user_following_servers = user.following_server.values('server')
            posts = Post.objects.filter(server__in=user_following_servers).order_by('-created').order_by('-votes_count')
        else:
            posts = Post.objects.order_by('-created').order_by('-votes_count')
        return render(request, 'home/hot.html', {'posts':posts})

def SearchAjaxView(request):
    if is_ajax(request=request):
        response = None
        searched_word = request.POST.get('searchedWord')
        servers = Server.objects.filter(tag__icontains=searched_word)
        users = User.objects.filter(username__icontains=searched_word)
        querysets = itertools.chain(users,servers)

        if len(users) > 0 or len(servers) > 0 and len(searched_word) > 0:
            data = []
            for qs in querysets:
                try:
                    item = {
                        'id':qs.id,
                        'username':qs.username,
                        'image': str(qs.profile.image.url),
                    }
                except:
                    item = {
                        'id':qs.id,
                        'tag':qs.tag,
                        'image': str(qs.image.url),
                        'followers_count': str(qs.followers.count())
                    }
                data.append(item)
            response = data
        else:
            response = 'no results found'
        return JsonResponse({'data':response})
    return JsonResponse({})