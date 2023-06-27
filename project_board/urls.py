"""project_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ckeditor_uploader.views import upload, browse
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url

from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import never_cache

urlpatterns = [
                  path('ckeditor/upload/', upload, name='ckeditor_upload'),
                  path(r'ckeditor/browse/', never_cache(browse), name='ckeditor_browse'),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('', include('posts.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


