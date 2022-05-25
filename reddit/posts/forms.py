from django.forms import ModelForm
from django import forms
from .models import Post


class UpdateCreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','video','image','text']
        widgets ={'title':forms.TextInput({'placeholder':'تیتر'}), 'text':forms.Textarea({'placeholder':'متن'})}
       
            

