from django.forms import ModelForm
from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','video','image','text']

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','video','image','text','server']
        widgets ={'title':forms.TextInput({'placeholder':'تیتر'}), 'text':forms.Textarea({'placeholder':'متن'})}    
    
    def clean(self, text = None,video=None):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        video = cleaned_data.get("video")
        image = cleaned_data.get("image")
        if (text != '' and video is not None) or (text != '' and image is not None) or (video is not None and image is not None) :
            raise ValidationError('فقط یک نوع پست قابل قبول است')

# class ChooseServerForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['server']