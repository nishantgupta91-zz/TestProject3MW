"""mysite URL Configuration

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

urlpatterns = [
    url(r'^$', 'demo.views.home', name='home'),
    url(r'^sites/(?P<pk>[0-9]+)/$', 'demo.views.sites_details'),
    url(r'^sites', 'demo.views.sites', name='sites'),
    url(r'^sum_summary', 'demo.views.sum_summary', name='sum_summary'),
    url(r'^average_summary', 'demo.views.average_summary', name='average_summary'),
]
