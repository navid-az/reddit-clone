from django.dispatch import receiver
from django.db.models.signals  import post_save
from .models import Server, ServerModerator

@receiver(post_save, sender=Server)
def creator_to_moderator(instance, *args, **kwargs):
    server = Server.objects.get(pk=instance.id)
    moderator = ServerModerator.objects.filter(user=instance.creator)
    if not moderator.exists():
      ServerModerator.objects.create(user=instance.creator)
    ass = ServerModerator.objects.get(user=instance.creator)
    ass.server.add(server)