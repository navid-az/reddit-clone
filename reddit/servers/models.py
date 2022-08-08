from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from colorfield.fields import ColorField

# Create your models here.
class Server(models.Model):
    SERVER_CHOICES = (
        ('pub', 'عمومی'),
        ('pri', 'شخصی'),
    )
    creator = models.ForeignKey(User , on_delete=models.CASCADE, related_name='user_servers')
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    about = models.TextField(default='about')
    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(default='server')
    image = models.ImageField(upload_to='servers/pic/', default='https://play-lh.googleusercontent.com/nlptFyxNsb8J0g8ZLux6016kunduV4jCxIrOJ7EEy-IobSN1RCDXAJ6DTGP81z7rr5Zq')
    header_image = models.ImageField(upload_to='servers/header-pic/', default='https://play-lh.googleusercontent.com/nlptFyxNsb8J0g8ZLux6016kunduV4jCxIrOJ7EEy-IobSN1RCDXAJ6DTGP81z7rr5Zq')
    server_type = models.CharField(max_length=3, choices=SERVER_CHOICES, default='pri')
    members_count = models.IntegerField(default=0)
    online_count = models.IntegerField(default=0)
    required_karma = models.IntegerField(default=0)

    def __str__(self):
        return f'r/{self.tag} owned by {self.creator}'

class ServerFollow(models.Model):
    server = models.ForeignKey(Server ,on_delete=models.CASCADE, related_name='followers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_server')
    created = models.DateTimeField(auto_now_add=True)

class ServerTag(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=20)
    primary_color = ColorField(default = '#A50277')
    secondary_color = ColorField(default = '#FFB8EB')
    is_allowed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} --> r/{self.server}'

class ServerRule(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='rules')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)