from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from django.views import View

# Create your views here.
class UserRegister(View):
    form_class = RegisterForm
    template_name = 'accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'شما از قبل وارد شدید')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'شما با موفقیت عضو شدید!')
            return redirect('home:home')
        return render(request, self.template_name, {'form':form})


class UserLogin(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'شما از قبل وارد شدید')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, '!به ردیت خوش اومدی')
                return redirect('home:home')
            messages.error(request, '!رمز یا نام کاربریت اشتباهه')
        return render(request, self.template_name, {'form':form}) 

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form':form})    

class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.error(request, '!خروج از پروفایل انجام شد') 
        return redirect('home:home')

class UserProfile(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        return render(request, 'accounts/profile.html', {'user':user})
