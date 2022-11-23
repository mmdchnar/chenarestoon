"""chenarestoon URL Configuration

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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import handler404, handler500
from django.urls import path, include, re_path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views
from polls.views import files, chat, chat_logout

handler404 = 'polls.views.page_not_found'
handler500 = 'polls.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('polls/', include('polls.urls')),
    path('dl/', files, name='files'),
    path('chat', chat, name='chat'),
    path('chat/logout', chat_logout, name='chat_logout'),
    re_path(r'^(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]
