from django.contrib import admin
from .models import Server, ServerFollow, ServerPostTag, ServerUserTag, ServerRule, ServerModerator

admin.site.register(Server) 
admin.site.register(ServerFollow)
#moderating page
admin.site.register(ServerPostTag)
admin.site.register(ServerUserTag)
admin.site.register(ServerRule)
admin.site.register(ServerModerator)
