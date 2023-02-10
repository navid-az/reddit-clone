from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserProfileSettingsForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ('user',)
    widgets ={'name':forms.TextInput({'class':'name-field'}), 'bio':forms.Textarea({'class':'bio-field'}), 'image':forms.FileInput, 'header_image':forms.FileInput}

class UserPassChangeForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  new_password = forms.CharField(widget=forms.PasswordInput())
  confirm_new_password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = User
    fields = ['password']

  def clean(self):
    new_password = self.cleaned_data['new_password']
    confirm_new_password = self.cleaned_data['confirm_new_password']

    if new_password != confirm_new_password:
      raise forms.ValidationError("password and confirm_password does not match")

class UserEmailChangeForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  email = forms.CharField(widget=forms.TextInput())
  class Meta:
    model = User
    fields = ['email', 'password']
