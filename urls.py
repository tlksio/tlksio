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
from django.conf.urls import include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from tlksio import views as main_views
from talks import views as talk_views

urlpatterns = [
    url(r'^$', main_views.index, name='index'),
    url(r'^auth/login', main_views.login, name='login'),
    url(r'^auth/twitter/callback', main_views.auth_twitter_callback, name='auth_twitter_callback'),
    url(r'^auth/twitter', main_views.auth_twitter, name='auth_twitter'),
    url(r'^auth/logout', main_views.logout, name='logout'),
    url(r'^settings', main_views.settings, name='settings'),
    url(r'^profile/(?P<username>[\w-]+)$', main_views.profile, name='profile'),
    url(r'^profile/(?P<username>[\w-]+)/upvoted$', main_views.profile_upvoted, name='profile_upvoted'),
    url(r'^profile/(?P<username>[\w-]+)/favorited$', main_views.profile_favorited, name='profile_favorited'),
    url(r'^about', main_views.about, name='about'),
    url(r'^faq', main_views.faq, name='faq'),
    url(r'^contactus', main_views.contactus, name='contactus'),
    url(r'^terms', main_views.terms, name='terms'),
    url(r'^privacy', main_views.privacy, name='privacy'),
    url(r'^activity', main_views.activity, name='activity'),

    url(r'^latest', talk_views.latest, name='latest'),
    url(r'^popular', talk_views.popular, name='popular'),

    url(r'^tag/(?P<tag_slug>[\w-]+)', talk_views.tag, name='tag'),

    url(r'^talk/add$', talk_views.add, name='add'),
    url(r'^talk/play/(?P<talk_slug>[0-9]+)', talk_views.play, name='play'),
    url(r'^talk/favorite/(?P<talk_id>[0-9]+)', talk_views.favorite, name='favorite'),
    url(r'^talk/upvote/(?P<talk_id>[0-9]+)', talk_views.upvote, name='upvote'),
    url(r'^talk/(?P<talk_slug>[\w-]+)', talk_views.talk, name='talk'),

    url(r'^admin/', admin.site.urls),

    url(r'^search/', include('haystack.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
