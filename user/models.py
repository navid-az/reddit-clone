from django.db import models
from django.contrib.auth.models import User
from servers.models import ServerUserTag

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50, null=True, blank=True)
  karma = models.IntegerField(default=0, null=True, blank=True)
  image = models.ImageField(upload_to='users/pic/', null=True, blank=True, default='default/reddit-default-img.webp')
  header_image = models.ImageField(upload_to='users/header-pic/', null=True, blank=True, default='default/reddit-default-header-img.jpg')
  bio = models.TextField(null=True, blank=True)
  age = models.PositiveSmallIntegerField(null=True, blank=True)
  tag = models.ManyToManyField(ServerUserTag, blank=True, null=True)