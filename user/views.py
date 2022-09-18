from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.models import User
# from reddit.posts.models import Save
from .models import Profile
from django.contrib import messages
from .forms import UserProfileSettingsForm


class UserProfileView(View):
	def get(self, request, username):
		user = get_object_or_404(User, username=username)
		posts = user.posts.all()
		comments = user.user_comments.all()
		return render(request, 'user/profile.html', {'posts':posts, 'comments':comments, 'user':user})

class UserProfileSettingsView(View):
	form_class = UserProfileSettingsForm

	def get(self, request, *args, **kwargs):
		form = self.form_class(instance=request.user.profile)
		return render(request, 'user/profile_settings.html', {'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			messages.success(request, '!پروفایل شما با موفقیت ویرایش شد')
		return redirect('user:profile', request.user.id)

class UserSavedPostsView(View):
	def get(self, request, username):
		user = User.objects.get(username=username)
		saved_posts = user.user_saves.all()
		# is_saved = Save.objects.filter(post=self.post_instance, user=request.user.id)
		return render(request, 'user/saved_posts.html', {'saved_posts':saved_posts})
