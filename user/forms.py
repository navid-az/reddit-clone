from django import forms
from .models import Profile

class UserProfileSettingsForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user',)
    widgets ={'name':forms.TextInput({'class':'name-field'}), 'bio':forms.Textarea({'class':'bio-field'}), 'image':forms.FileInput, 'header_image':forms.FileInput}
  