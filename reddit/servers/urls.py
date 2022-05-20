from django.urls import path
from .views import Servers

app_name= 'servers'

urlpatterns = [
    path('', Servers.as_view(), name='servers' )
]
