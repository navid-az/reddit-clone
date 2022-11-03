from genericpath import exists
from django.dispatch import receiver
from django.db.models.signals  import post_save
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile_signal(instance, *args, **kwargs):
  user = User.objects.get(id=instance.id)
  profile = Profile.objects.filter(user=user)
  if not profile.exists():
    new_profile = Profile(user=user, name='hello')
    new_profile.save()