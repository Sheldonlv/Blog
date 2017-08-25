"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from base import views as base
from body import views as body

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',base.index),
    url(r'^about',base.about),
    url(r'^essay',base.essay),
    url(r'^time',body.time),
    url(r'^article',body.article),
    url(r'^gustbook',body.gustbook),
    url(r'edit',body.edit),
]
