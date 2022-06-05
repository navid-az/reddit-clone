from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
  model = Profile
  can_delete = False

class ExtendedUserAdmin(UserAdmin):
  inlines = [ProfileInline]

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
# admin.site.register(Profile)
