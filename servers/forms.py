from django import forms
from .models import Server, ServerModerator, ServerRule, ServerPostTag, ServerUserTag, ServerModeratorPermission

class CreateServerForm(forms.ModelForm):
  class Meta:
    model = Server
    fields = ['tag', 'server_type']
    widgets = {'server_type':forms.RadioSelect({'class':'server-type-button'})}

class CreatePostTagForm(forms.ModelForm):
  class Meta:
    model = ServerPostTag
    exclude = ['is_allowed', 'server', 'creator']

class CreateUserTagForm(forms.ModelForm):
  class Meta:
    model = ServerUserTag
    exclude = ['is_allowed', 'server', 'user', 'creator']

class CreateRuleForm(forms.ModelForm):
  class Meta:
    model = ServerRule
    exclude = ['created', 'server', 'creator']

class UpdateModeratorPermissionsForm(forms.ModelForm):
  class Meta:
    model = ServerModeratorPermission
    exclude = ['server', 'moderator']

class AddModeratorForm(forms.ModelForm):
  class Meta:
    model = ServerModerator
    fields = ['user']