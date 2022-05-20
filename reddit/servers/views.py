from django.shortcuts import render
from django.views import View
from .models import Server

# Create your views here.
class Servers(View):
    def get(self, request):
        servers = Server.objects.all()
        return render(request, 'home/home.html',{'servers':servers})