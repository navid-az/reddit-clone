from django.urls import path
from .views import UserLogout, UserPasswordResetCompleteView, UserPasswordResetSuccessView, UserPasswordResetView, UserRegister, UserLogin, UserPasswordResetConfirmView

app_name = 'accounts'

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('reset/success/', UserPasswordResetSuccessView.as_view(), name='password_reset_success'),
    path('confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm' ),
    path('confirm/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete' )
]
