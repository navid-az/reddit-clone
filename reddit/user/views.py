from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(View):
	def get(self, request, pk):
		user = User.objects.get(pk=pk)
		posts = Post.objects.filter(creator=user)
		return render(request, 'user/profile.html', {'user':user, 'posts':posts})
