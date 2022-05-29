from django.shortcuts import get_object_or_404, render
from django.views import View
from django.contrib.auth.models import User


class UserProfileView(View):
	def get(self, request, pk):
		user = get_object_or_404(User, id=pk)
		posts = user.posts.all()
		return render(request, 'user/profile.html', {'posts':posts})
