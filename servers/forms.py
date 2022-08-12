from django import forms
from .models import Server, ServerRule, ServerPostTag, ServerUserTag

class CreateServerForm(forms.ModelForm):
  class Meta:
    model = Server
    fields = ['tag', 'server_type']
    widgets = {'server_type':forms.RadioSelect({'class':'server-type-button'})}

class CreatePostTagForm(forms.ModelForm):
  class Meta:
    model = ServerPostTag
    exclude = ['is_allowed', 'server']
class CreateUserTagForm(forms.ModelForm):
  class Meta:
    model = ServerUserTag
    exclude = ['is_allowed', 'server']

class CreateRuleForm(forms.ModelForm):
  class Meta:
    model = ServerRule
    exclude = ['created', 'server', 'creator']