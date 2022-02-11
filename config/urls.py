from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brand/', include('brand.urls')),
    path('post/', include('post.urls')),
    path('accounts/',include('allauth.urls')),
    re_path(r'^upload/', views_ckeditor.upload, name='ckeditor_upload'),
    re_path(r'^browse/', never_cache((views_ckeditor.browse)), name='ckeditor_browse'),
    path('', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)