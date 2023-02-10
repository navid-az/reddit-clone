from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from posts.models import Post, Comment
from .models import Profile
from django.contrib import messages
from .forms import UserProfileSettingsForm, UserPassChangeForm, UserEmailChangeForm
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin


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

class UserProfileSettingsView(LoginRequiredMixin, View):
	profile_form_class = UserProfileSettingsForm
	user_pass_change_form_class = UserPassChangeForm
	user_email_change_form_class = UserEmailChangeForm

	def setup(self, request, *args, **kwargs):
		self.user = get_object_or_404(User, username=kwargs['username'])
		self.user_info = get_object_or_404(Profile, user=self.user)
		return super().setup(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		profile_form = self.profile_form_class(instance=self.user_info)
		change_pass_form = self.user_pass_change_form_class()
		change_email_form = self.user_email_change_form_class()
		return render(request, 'user/profile_settings.html', {'profile_form':profile_form, 'change_pass_form':change_pass_form, 'change_email_form':change_email_form})

	def post(self, request, *args, **kwargs):
		profile_form = self.profile_form_class(request.POST, request.FILES, instance=self.user_info)
		change_pass_form = UserPassChangeForm(request.POST)
		change_email_form = UserEmailChangeForm(request.POST)
		print(('profile_form' in request.POST),'$$$$$$$$$$$$4',('change_pass_form' in request.POST),'%%%%',('change_email_form' in request.POST))

		if ('profile_form' in request.POST) and profile_form.is_valid():
			updated_info = profile_form.save(commit=False)
			updated_info.user = self.user
			updated_info.save()
			messages.success(request, '!پروفایل شما با موفقیت ویرایش شد')
			return redirect('user:profile', request.user.username)
		elif ('change_pass_form' in request.POST) and change_pass_form.is_valid():
			password = self.user.check_password(str(request.POST['password']))
			
			if password:
				self.user.set_password(str(request.POST['new_password']))
				self.user.save()
				messages.success(request, '!رمز عبور با موفقیت تغییر کرد')
				return redirect('home:home')
			else:
				messages.error(request, 'wtf is this shit???')
				return redirect('user:profile', request.user.username)
		elif ('change_email_form' in request.POST) and change_email_form.is_valid():
			password = self.user.check_password(str(request.POST['password']))
			if password:
				new_email = change_email_form.save(commit=False)
				new_email.email = request.POST['email']
				new_email.save()
				messages.success(request, '!ایمل با موفقیت تغییر کرد')
				return redirect('user:profile', request.user.username)
		return render(request, 'user/profile_settings.html', {'profile_form':profile_form})

class UserSavedPostsView(View):
	def get(self, request, username):
		user = User.objects.get(username=username)
		saved_posts = user.user_saves.filter(value='save')
		return render(request, 'user/saved_posts.html', {'saved_posts':saved_posts})