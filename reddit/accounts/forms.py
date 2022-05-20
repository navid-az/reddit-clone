from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


labels = ['نام کاربری', 'ایمیل', 'رمز عبور']
errors = {'required': 'این فیلد اجباری میباشد', 'invalid': 'این ایمیل اشتباه است'}

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label=labels[0], error_messages={'required':errors['required']})
    email = forms.EmailField(label=labels[1], error_messages={'required':errors['required'], 'invalid':errors['invalid']})
    password = forms.CharField(max_length=50, label=labels[2], widget=forms.PasswordInput, error_messages={'required':errors['required']})

    def clean_username(self):
        data = self.cleaned_data['username']
        user = User.objects.filter(username=data)
        if user:
            raise ValidationError('این نام کاربری در ردیت وجود دارد')
        return data

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل قبلا در ریدیت ثبت شده')
        return email
            

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label=labels[0], error_messages={'required':errors['required']})
    password = forms.CharField(max_length=50, label=labels[2], widget=forms.PasswordInput, error_messages={'required':errors['required']})