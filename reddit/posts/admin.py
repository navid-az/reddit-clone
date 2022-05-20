from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'creator', 'server')
    search_fields = ('title', 'creator', 'server')
    list_filter= ['created']


admin.site.register(Comment)
