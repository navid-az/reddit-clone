from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50, null=True, blank=True)
  image = models.ImageField(upload_to='users/pic/', null=True, blank=True)
  header_image = models.ImageField(upload_to='users/header-pic/', null=True, blank=True)
  bio = models.TextField(null=True, blank=True)
  age = models.PositiveSmallIntegerField(null=True, blank=True)