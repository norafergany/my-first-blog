"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib import admin
from django.urls import include, path, re_path
import blog

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^accounts/login/$', views.login, name='login'),
#     url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
#     url(r'', blog.urls),
# ]

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    re_path('^accounts/login/$', views.LoginView, name='login'),
    re_path('^accounts/logout/$', views.LogoutView, name='logout', kwargs={'next_page': '/'}),
]