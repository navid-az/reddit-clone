from django.forms import ModelForm, Textarea
from django import forms
from .models import Post, Comment
from django.core.exceptions import ValidationError


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','video','image','text']

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','video','image','text','server']
        widgets ={'title':forms.TextInput({'placeholder':'تیتر'}), 'text':forms.Textarea({'placeholder':'متن'}), 'server':forms.Select({'id':'server-field'})}    
    
    def clean(self, text = None,video=None):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        video = cleaned_data.get("video")
        image = cleaned_data.get("image")
        if (text != '' and video is not None) or (text != '' and image is not None) or (video is not None and image is not None) :
            raise ValidationError('فقط یک نوع پست قابل قبول است')

class CreateCommentReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {'body': Textarea(attrs={'id':'comment-form'})}

    