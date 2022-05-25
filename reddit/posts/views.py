from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views import View
from .forms import UpdateCreatePostForm
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

class PostPageView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, id = pk)
        # comments_count = len(Comment.objects.filter(post = post))
        comments = Comment.objects.filter(post=post)
        return render(request, 'posts/post-page.html',{'post':post, 'comments':comments})
       
class CreatePostView(LoginRequiredMixin, View):
    form_class = UpdateCreatePostForm

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        if not user.id == request.user.id:
            messages.error(request, 'تو کی هستی دیگه شومبول؟')
            return redirect('home:hoem')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        form = self.form_class()
        return render(request, 'posts/create-post.html', {'form':form})

    def post(self, request, pk):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid:
            saved_form = form.save(commit=False)
            saved_form.creator = request.user
            saved_form.save()
            messages.success(request, 'پست شما باموفقیت ایجاد شد')
            return redirect('home:home')
        return render(request, 'posts/create-post.html', {'form':form})

def post_tab(request):
        return JsonResponse({"text":"niggaass"})


class UpdatePostView(LoginRequiredMixin, View):

    form_class = UpdateCreatePostForm

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
