"""diquest_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('support/', include('support.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import HomeView, UserCreateView, UserCreateDoneTV



urlpatterns = [
    path('admin/', admin.site.urls),

    # shkim
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('', HomeView.as_view(), name='home'),
    path('product/', include('product.urls')),
    path('support/', include('support.urls')),
    path('photo/', include('photo.urls')),
    path('morpheme/', include('morpheme.urls')),
    path('ml/', include('ml.urls')),
    path('rtc/', include('rtc.urls')),

    path('accounts/register/add/', UserCreateDoneTV.as_view(), name='register_add')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
