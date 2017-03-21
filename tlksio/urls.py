"""tlksio URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from . import views
from talks import views as talk_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^faq', views.faq, name='faq'),
    url(r'^contactus', views.contactus, name='contactus'),
    url(r'^terms', views.terms, name='terms'),
    url(r'^privacy', views.privacy, name='privacy'),

    url(r'^latest', talk_views.latest, name='latest'),
    url(r'^popular', talk_views.popular, name='popular'),

    url(r'^admin/', admin.site.urls),
]
