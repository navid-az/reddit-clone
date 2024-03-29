from django.contrib import admin
from .models import Post, Comment, CommentVote, PostVote, PostSave, ReportPost
from mptt.admin import MPTTModelAdmin

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'creator', 'server', 'id')
    search_fields = ('title', 'creator', 'server')
    list_filter= ['created']


# admin.site.register(Comment)
admin.site.register(Comment, MPTTModelAdmin)
admin.site.register(PostVote)
admin.site.register(CommentVote)
admin.site.register(PostSave)
admin.site.register(ReportPost)
