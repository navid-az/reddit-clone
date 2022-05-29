from django.db import models
from servers.models import Server
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# if you put the child model on top of the parent model-
# -(comment is a child to the post because of the foreignkey) you need to put Post inside quotation marks to make it work 
class Comment(models.Model):
    body = models.TextField(max_length=800)
    created = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=1, related_name='post_comments')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='user_comments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    is_reply = models.BooleanField(default=False)

class Post(models.Model):
    post_type_choices = [('text', 'text'), ('video', 'video'), ('image', 'image'), ('link','link')]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='nigag')
    text = models.TextField(null=True, blank=True)
    text_allowed = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    image_allowed = models.BooleanField(default=True)
    video = models.FileField(upload_to='posts/videos/', null=True, blank=True)
    video_allowed = models.BooleanField(default=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, default=1, related_name='posts')
    creator = models.ForeignKey(User , on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=5, choices=post_type_choices, default='text')
    vote_count = models.IntegerField(default=0)
    upvote = models.ManyToManyField(User, related_name='upvote')
    downvote = models.ManyToManyField(User, related_name='downvote')

    def get_absolute_url(self):
        return reverse("posts:post-page", args={self.id})

    def get_profile_page(self):
        return reverse("user:profile", args={self.creator.id})
    
    def __str__(self):
        return f"{self.title} - {self.creator}"

