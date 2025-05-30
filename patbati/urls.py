"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.reverse import reverse_lazy
from django.contrib.auth import views as auth_views



admin.autodiscover()

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('bati:bati_list'), permanent=True), name='home'),
    path('', include("patbati.bati.urls")),
    path('', include('mapentity.urls')),
    path('paperclip/', include('paperclip.urls')),
    path("admin/", admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': '/'}, name='logout',),
]
