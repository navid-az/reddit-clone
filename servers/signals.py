from django.dispatch import receiver
from django.db.models.signals  import post_save
from .models import Server, ServerFollow, ServerModerator, ServerModeratorPermission, ServerUserLimitation

@receiver(post_save, sender=Server)
def creator_to_moderator(instance, *args, **kwargs):
  server = Server.objects.get(pk=instance.id)
  moderator = ServerModerator.objects.filter(user=instance.creator)
  if not moderator.exists():
    ServerModerator.objects.create(user=instance.creator)
  new_moderator = ServerModerator.objects.get(user=instance.creator)
  new_moderator.server.add(server)
  permission = ServerModeratorPermission.objects.filter(server=server, moderator=new_moderator)
  if not permission:
    ServerModeratorPermission.objects.create(server=server, moderator=new_moderator, allow_create_tag=True
    , allow_delete_tag=True, allow_create_rule=True, allow_delete_rule = True, allow_remove_user = True
    , allow_remove_moderator = True, allow_delete_post = True)

  
# ban user from server
@receiver(post_save, sender=ServerUserLimitation)
def unFollowServer(instance, *args, **kwargs):
  following = ServerFollow.objects.get(server=instance.server, user=instance.user)
  following.delete()