from django.contrib import admin
from .models import Server, ServerFollow, ServerTag

# Register your models here.
admin.site.register(Server) 
admin.site.register(ServerFollow)
admin.site.register(ServerTag)
