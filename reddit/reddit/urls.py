from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('servers/', include('servers.urls', namespace='servers')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('u/', include('user.urls', namespace='user'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
