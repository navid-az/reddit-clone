from django import forms
from .models import Server

class CreateServerForm(forms.ModelForm):
  class Meta:
    model = Server
    fields = ['tag', 'server_type']
    widgets = {'server_type':forms.RadioSelect({'class':'server-type-button'})}
