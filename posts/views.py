from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views import View
from .forms import UpdatePostForm, CreatePostForm, CreateCommentReplyForm
from .models import Post, Comment, Vote, PostSave
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from servers.models import Server, ServerFollow, ServerUserTag
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F
from django.http import JsonResponse
from django.core import serializers

class PostPageView(View):
    form_class = CreateCommentReplyForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, id=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        is_saved = PostSave.objects.filter(post=self.post_instance, user=request.user.id)
        comments = self.post_instance.post_comments.filter(is_reply=False)
        return render(request, 'posts/post-page.html',{'post':self.post_instance, 'comments':comments, 'form':form, 'is_saved':is_saved})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.creator = request.user
            new_comment.post = self.post_instance
            new_comment.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد')
            return redirect('posts:post-page', self.post_instance.id)

class CreateReplyView(LoginRequiredMixin, View):
    form_class = CreateCommentReplyForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, id=kwargs['post_id'])
        self.comment_instance = get_object_or_404(Comment, id=kwargs['comment_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'posts/post-page.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.creator = request.user
            reply.post = self.post_instance
            reply.parent = self.comment_instance
            reply.save()
            messages.success(request, 'your reply to a reply has been saved!')
            return redirect('posts:post-page', self.post_instance.id)

class CreatePostView(LoginRequiredMixin, View):
    form_class = CreatePostForm
    # server_form = ChooseServerForm

    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(id=kwargs['pk'])
        if not user.id == request.user.id:
            messages.error(request, 'شما نمیتوانید پست ایجاد کنید')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        following = ServerFollow.objects.filter(user=request.user)
        form = self.form_class()
        return render(request, 'posts/create-post.html', {'form':form, 'following':following})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        following = ServerFollow.objects.filter(user=request.user)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.creator = request.user
            saved_form.save()
            # servers.save()
            messages.success(request, 'پست شما باموفقیت ایجاد شد')
            return redirect('home:home')
        return render(request, 'posts/create-post.html', {'form':form, 'following':following})

class CreatePostAjaxView(View):
    def get(self, request, server_tag):
        server = Server.objects.get(tag=server_tag)
        server_tags = server.post_tags.all()
        server_rules = server.rules.all()
        serialized_server = serializers.serialize("python", {server})
        data = [serialized_server]
        for i in server_tags:
            tags={
            'id':i.id,
            'name':i.name,
            'primary_color':i.primary_color,
            'secondary_color':i.secondary_color
            }
            data.append(tags)
        for j in server_rules:
            rules={
            'title':j.title,
            'body':j.body,
            }
            data.append(rules)
        return JsonResponse({'data':data})
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
        post = Post.objects.get(pk=pk)
        if post.creator.id == request.user.id:
            post.delete()
            messages.success(request, '!پست با موفقیت حذف شد')
        else:
            messages.error('شما نمیتوانید پست دیگران را حذف کنید')
        return redirect('user:profile', request.user.username)
        
def savePostAjaxView(request):
    if request.method == 'POST':
        post_id = request.POST.get('postId')
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=request.user.id)

        if user in post.saved.all():
            post.saved.remove(user)
        else:
            post.saved.add(user)
        
        save_post, created = PostSave.objects.get_or_create(post=post, user=user)
        if not created:
            if save_post.value=='save':
                save_post.value='unsave'
            else:
                save_post.value='save'
        else:
            save_post.value='save'  
        post.save()
        save_post.save()
    return redirect('home:home')

def votePostAjaxView(request):
    if request.method == 'POST':
        post_id = request.POST.get('postId')
        vote_type = request.POST.get('voteType')
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=request.user.id)
        # if user in post.upvotes.all():
        #     post.upvotes.remove(user)
        # else:
        #     post.saved.add(user)

        vote, created = Vote.objects.get_or_create(post=post, user=user)
        
        if not created:
            if vote.choice == 'up' and vote_type == 'downvote':
                post.downvotes.add(user)
                post.upvotes.remove(user)
                post.votes_count = F('votes_count') - 2
                vote.choice = 'down'
                post.save()
                vote.save()
            elif vote.choice == 'down' and vote_type == 'upvote':
                post.downvotes.remove(user)
                post.upvotes.add(user)
                post.votes_count = F('votes_count') + 2
                vote.choice = 'up'
                post.save()
                vote.save()
            else:
                if vote.choice == 'up':
                    post.votes_count = F('votes_count') - 1
                else:
                    post.votes_count = F('votes_count') + 1

                post.upvotes.remove(user)
                post.downvotes.remove(user)
                post.save()
                vote.delete()
        else:
            if vote_type == 'upvote':
                post.votes_count = F('votes_count') + 1
                post.upvotes.add(user)
                vote.choice = 'up'
            else:
                post.votes_count = F('votes_count') - 1
                post.downvotes.add(user)
                vote.choice = 'down'

            post.save()
            vote.save()
    return redirect('home:home')

# class UpVotePostView(LoginRequiredMixin, View):
#     def get(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         upvote = Vote.objects.filter(post=post, user=request.user, choice='up')
#         downvote = Vote.objects.filter(post=post, user=request.user, choice='down')
#         if upvote.exists():
#             post.votes_count = F('votes_count') - 1
#             post.save()
#             upvote.delete()
#             messages.warning(request, 'you have already upvoted this post')
#             return redirect('posts:post-page', post_id)
#         elif downvote.exists():
#             post.votes_count = F('votes_count') + 2
#             post.save()
#             downvote.delete()
#             Vote(post=post, user=request.user, choice='up').save()
#             return redirect('posts:post-page', post_id)
#         elif not upvote.exists() and not downvote.exists():
#             post.votes_count = F('votes_count') + 1
#             post.save()
#             Vote(post=post, user=request.user, choice='up').save()
#             return redirect('posts:post-page', post_id)

            
# class DownVotePostView(LoginRequiredMixin, View):
#     def get(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         upvote = Vote.objects.filter(post=post, user=request.user, choice='up')
#         downvote = Vote.objects.filter(post=post, user=request.user, choice='down')
#         if upvote.exists():
#             post.votes_count = F('votes_count') - 2
#             post.save()
#             upvote.delete()
#             Vote(post=post, user=request.user, choice='down').save()
#             return redirect('posts:post-page', post_id)
#         elif downvote.exists():
#             post.votes_count = F('votes_count') + 1
#             post.save()
#             downvote.delete()
#             messages.warning(request, 'you have already downvoted this post')
#             return redirect('posts:post-page', post_id)
#         elif not upvote.exists() and not downvote.exists():
#             post.votes_count = F('votes_count') - 1
#             post.save()
#             Vote(post=post, user=request.user, choice='down').save()
#             return redirect('posts:post-page', post_id)

# class PostSavePostView(LoginRequiredMixin ,View):
#     def get(self, request, post_id):
#         post = Post.objects.get(id=post_id)
#         saved_post = PostSave.objects.filter(post=post, user=request.user)
#         if saved_post.exists():
#             saved_post.delete()
#             return redirect('posts:post-page', post_id)
#         PostSave(post=post, user=request.user).save()
#         messages.success(request, '!پست مورد نظر با موفقیت ذخیره شد')
#         return redirect('posts:post-page', post_id)
