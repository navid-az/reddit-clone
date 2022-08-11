from xmlrpc.client import Server
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from posts.models import Post, Save
from servers.models import Server

# Create your views here.
class Home(View):
    def get(self, request):
        posts = Post.objects.all()
        servers = Server.objects.all()
        if request.user.is_authenticated:
            is_saved = Save.objects.filter(user=request.user.id)
            return render(request, 'home/home.html',{'servers':servers, 'posts':posts, 'is_saved':is_saved})
        else:
            return render(request, 'home/home.html',{'servers':servers, 'posts':posts})
            

class NewPosts(View):
    def get(self, request):
        posts = Post.objects.order_by('-created')
        return render(request, 'home/new.html', {'posts':posts})
        # data = []
        # for hot in hot_posts:
        #     item = {
        #         'id': hot.id,
        #         'title': hot.title,
        #         'created': hot.created,
        #         'text': hot.text,
        #         'server': hot.server.name,
        #         'creator': hot.creator.username,
        #         'server_image' : hot.server.image.url,
        #     }
        #     if hot.image.url is not None:
        #         item['image'] = hot.image.url
            
        #     data.append(item)
        # return JsonResponse({'data':data})
