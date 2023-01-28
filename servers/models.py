from django.db import models
from django.contrib.auth.models import User, Group
from django.forms import CharField
from colorfield.fields import ColorField
from django.db.models import Q

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
    image = models.ImageField(upload_to='servers/pic/', default='default/reddit.jpg')
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
    updated = models.DateTimeField(auto_now=True)


class ServerPostTag(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='post_tags')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_tags')
    name = models.CharField(max_length=20)
    primary_color = ColorField(default = '#A50277')
    secondary_color = ColorField(default = '#FFB8EB')
    is_allowed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} --> r/{self.server}'


class ServerUserTag(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='user_tags')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tags')
    user = models.ManyToManyField(User, related_name='user_tag')
    name = models.CharField(max_length=20)
    primary_color = ColorField(default = '#A50277')
    secondary_color = ColorField(default = '#FFB8EB')
    is_allowed = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} --> r/{self.server}'


class ServerRule(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='rules')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rules')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} | made by {self.creator} for r/{self.server.tag}'


class ServerModerator(models.Model):
    server = models.ManyToManyField(Server, related_name='moderator_of', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moderator_of')

    def is_moderator(self):
        moderator = ServerModerator.objects.filter(user=self.user, server=self.server)

    def __str__(self) -> str:
        return f'{self.user.username}'


class ServerModeratorPermission(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='permissions', default=0)
    moderator = models.ForeignKey(ServerModerator, on_delete=models.CASCADE, related_name='permissions')
    allow_delete_tag = models.BooleanField(default=False)
    allow_create_tag = models.BooleanField(default=True)
    allow_delete_rule = models.BooleanField(default=False)
    allow_update_rule = models.BooleanField(default=False)
    allow_create_rule = models.BooleanField(default=False)
    allow_remove_moderator = models.BooleanField(default=False)
    allow_add_moderator = models.BooleanField(default=False)
    allow_delete_report = models.BooleanField(default=True)
    allow_ban_user = models.BooleanField(default=True)
    allow_remove_user = models.BooleanField(default=False)
    allow_delete_post = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.moderator} moderator of r/{self.server.tag}'

class ServerUserLimitation(models.Model):
    LIMITATION_DURATION = (
        ('1', '۱ روز'),
        ('2', '۲ روز'),
        ('7', '۷ روز'),
        ('14', '۱۴ روز'),
        ('30', '۳۰ روز'),
        ('permanent', 'برای همیشه'),
    )
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name='limited_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='limited_from')
    duration = models.CharField(choices=LIMITATION_DURATION, default='1', max_length=9)
    info = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user} has been limited to post on {self.server} server for the duration of {self.duration}(day/days)'