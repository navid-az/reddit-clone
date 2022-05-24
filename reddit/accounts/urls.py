from django.urls import path
from .views import UserLogout, UserRegister, UserLogin

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
]
