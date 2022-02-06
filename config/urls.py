from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brand/', include('brand.urls')),
    path('post/', include('post.urls')),
    path('users/',include('users.urls')),
    path('accounts/',include('allauth.urls')),
    path('', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)