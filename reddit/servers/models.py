from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.
class Server(models.Model):
    SERVER_CHOICES = (
        ('pri', 'عمومی'),
        ('pub', 'شخصی'),
    )
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    about = models.TextField(default='about')
    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(default='server')
    image = models.ImageField(upload_to='servers/pic/')
    header_image = models.ImageField(upload_to='servers/header-pic/')
    server_type = models.CharField(max_length=3, choices=SERVER_CHOICES, default='pri')
    members_count = models.IntegerField(default=0)
    online_count = models.IntegerField(default=0)
    required_karma = models.IntegerField(default=0)

    def __str__(self):
        return f'r/{self.tag} owned by {self.creator}'

class ServerFollow(models.Model):
    server = models.ForeignKey(Server ,on_delete=models.CASCADE, related_name='followers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_server')
    created = models.DateTimeField(auto_now=True)

class ServerTag(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=20)
    primary_color = ColorField(default = '#ffff')
    secondary_color = ColorField(default = '#ffff')
    is_allowed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} --> r/{self.server}'