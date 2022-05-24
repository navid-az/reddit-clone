from django.db import models
from servers.models import Server
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    post_type_choices = [('text', 'text'), ('video', 'video'), ('image', 'image'), ('link','link')]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='nigag')
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    video = models.FileField(upload_to='posts/videos/', null=True, blank=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, default=1)
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=5, choices=post_type_choices, default='text')
    vote_count = models.IntegerField(default=0)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("posts:post-page", args={self.id})

    def get_profile_page(self):
        return reverse("user:profile", args={self.creator.id})
    
    def __str__(self):
        return f"{self.title} - {self.creator}"

class Comment(models.Model):
    body = models.TextField(default='comment body')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time = models.DateTimeField(auto_now=True)
