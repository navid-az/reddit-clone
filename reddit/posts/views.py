from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views import View
from .forms import UpdatePostForm, CreatePostForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

class PostPageView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, id = pk)
        comments = post.post_comments.filter(is_reply=False)
        return render(request, 'posts/post-page.html',{'post':post, 'comments':comments})
       
class CreatePostView(LoginRequiredMixin, View):
    form_class = CreatePostForm
    # server_form = ChooseServerForm

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        if not user.id == request.user.id:
            messages.error(request, 'شما نمیتوانید پست ایجاد کنید')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        form = self.form_class()
        # servers = self.server_form()
        return render(request, 'posts/create-post.html', {'form':form})

    def post(self, request, pk):
        form = self.form_class(request.POST, request.FILES)
        # servers = self.server_form(request.POST)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.creator = request.user
            saved_form.save()
            # servers.save()
            messages.success(request, 'پست شما باموفقیت ایجاد شد')
            return redirect('home:home')
        return render(request, 'posts/create-post.html', {'form':form})


class UpdatePostView(LoginRequiredMixin, View):

    form_class = UpdatePostForm

    def dispatch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if not post.creator.id == request.user.id:
            messages.error(request, '.شما نمیتوانید پست دیگران را ویرایش کنید')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class(instance=post)
        return render(request, 'posts/update-post.html', {'form':form, 'post':post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=post)
        if form.is_valid and request.FILES == None:
            form.save()
            messages.success(request, '!پست با موفقیت ویرایش شد')
            return redirect('posts:post-page', post.id)
        else:
            post.delete()
            messages.error(request, 'that shit was empty!')
            return redirect('home:home')
class DeletePostView(LoginRequiredMixin ,View):
    def get(self, request, pk):
        post = get_object_or_404(Post ,pk=pk)
        if post.creator.id == request.user.id:
            post.delete()
            messages.success(request, '!پست با موفقیت حذف شد')
        else:
            messages.error('شما نمیتوانید پست دیگران را حذف کنید')
        return redirect('user:profile', request.user.id)

# comment section