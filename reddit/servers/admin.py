from django.contrib import admin
from .models import Server, ServerFollow, ServerTag, ServerRule

admin.site.register(Server) 
admin.site.register(ServerFollow)
#moderating page
admin.site.register(ServerTag)
admin.site.register(ServerRule)
