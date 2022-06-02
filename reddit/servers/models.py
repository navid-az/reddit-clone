from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Server(models.Model):
    creator = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    slug = models.SlugField(default='server')
    description = models.TextField(default='hello')
    image = models.ImageField(upload_to='servers/pic/')
    header_image = models.ImageField(upload_to='servers/header-pic/')
    nsfw = models.BooleanField()
    members_count = models.IntegerField(default=0)
    online_count = models.IntegerField(default=0)
    required_karma = models.IntegerField(default=0)

    def __str__(self):
        return self.name


