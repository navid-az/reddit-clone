from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.models import User

from posts.models import Post, Comment
from .models import Profile
from django.contrib import messages
from .forms import UserProfileSettingsForm
from django.db.models import Sum


class UserProfileView(View):
	def get(self, request, username):
		user = get_object_or_404(User, username=username)
		posts = user.posts.all()
		comments = user.user_comments.all()

		comments = Comment.objects.filter(creator=user)
		posts = Post.objects.filter(creator=user)
		if comments.exists() or posts.exists():
			comment = comments.aggregate(Sum('votes_count'))
			post = posts.aggregate(Sum('votes_count'))
			karma = int((comment["votes_count__sum"]+post["votes_count__sum"])/5)

			user.profile.karma = karma
			user.profile.save()
		return render(request, 'user/profile.html', {'posts':posts, 'comments':comments, 'user':user})

class UserProfileSettingsView(View):
	form_class = UserProfileSettingsForm

	def setup(self, request, *args, **kwargs):
		self.user = get_object_or_404(User, username=kwargs['username'])
		self.user_info = get_object_or_404(Profile, user=self.user)
		return super().setup(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		form = self.form_class(instance=self.user_info)
		return render(request, 'user/profile_settings.html', {'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES, instance=self.user_info)
		print('$$$$$$$$$$$$$$$$$$$$$$$', request.FILES)
		if form.is_valid():
			updated_info = form.save(commit=False)
			updated_info.user = self.user
			updated_info.save()
			messages.success(request, '!پروفایل شما با موفقیت ویرایش شد')
			return redirect('user:profile', request.user.username)
		return render(request, 'user/profile_settings.html', {'form':form})

class UserSavedPostsView(View):
	def get(self, request, username):
		user = User.objects.get(username=username)
		saved_posts = user.user_saves.filter(value='save')
		return render(request, 'user/saved_posts.html', {'saved_posts':saved_posts})