from django.db import models
from servers.models import Server
from django.contrib.auth.models import User
from django.urls import reverse
from servers.models import ServerPostTag
from mptt.models import MPTTModel, TreeForeignKey

# if you put the child model on top of the parent model-
# -(comment is a child to the post because of the foreignkey) you need to put Post inside quotation marks to make it work 
class Comment(MPTTModel):
    body = models.TextField(max_length=800)
    created = models.DateTimeField(auto_now=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=1, related_name='post_comments')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='user_comments')
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return f'comment by {self.id} {self.creator}'
    class MPTTMeta:
        order_insertion_by = ['created']

class Post(models.Model):
    post_type_choices = [('text', 'text'), ('video', 'video'), ('image', 'image'), ('link','link')]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default='slug')
    text = models.TextField(null=True, blank=True)
    text_allowed = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    image_allowed = models.BooleanField(default=True)
    video = models.FileField(upload_to='posts/videos/', null=True, blank=True)
    video_allowed = models.BooleanField(default=True)
    saved = models.ManyToManyField(User, blank=True, related_name='saves')
    upvotes = models.ManyToManyField(User, blank=True, related_name='upvotes')
    downvotes = models.ManyToManyField(User, blank=True, related_name='downvotes')
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='posts')
    creator = models.ForeignKey(User , on_delete=models.CASCADE, related_name='posts', null=True)
    created = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=5, choices=post_type_choices, default='text')
    votes_count = models.IntegerField(default=0)
    tag = models.ForeignKey(ServerPostTag, on_delete=models.CASCADE, null=True, blank=True, related_name='post')

    def get_absolute_url(self):
        return reverse("posts:post-page", args={self.id})

    def get_profile_page(self):
        return reverse("user:profile", args={self.creator.username})
    
    def __str__(self):
        return f"{self.title} - {self.creator}"

class Vote(models.Model):
    types =[('up','upvote'), ('down','downvote')]
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=4, choices=types)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.choice}voted post {self.post.title}"

class PostSave(models.Model):
    VALUE_CHOICES = (
    ('save', 'save'),
    ('unsave', 'unsave'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_saves')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_saves')
    value = models.CharField(choices=VALUE_CHOICES, max_length=8, default='save')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} saved {self.post}'