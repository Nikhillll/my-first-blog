"""new_pro URL Configuration

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
from django.conf.urls import patterns, include, url
from artical.views import HelloTemplate
from django.contrib import admin

urlpatterns = [
	url(r'^articles/',include('artical.urls')),
	url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'new_pro.views.login'),
    url(r'^accounts/auth/$', 'new_pro.views.auth_view'),
    url(r'^accounts/logout/$', 'new_pro.views.logout'),
    url(r'^accounts/loggedin/$', 'new_pro.views.loggedin'),
    url(r'^accounts/invalid/$', 'new_pro.views.invalid_login'),
    url(r'^accounts/register/$', 'new_pro.views.register_user'),
    url(r'^accounts/register_success/$', 'new_pro.views.register_success'),
    url(r'^accounts/contactus/$', 'new_pro.views.contactus'),
    url(r'^accounts/repeat_login/$', 'new_pro.views.repeat_login'),
    url(r'^accounts/repeat_logout/$', 'new_pro.views.repeat_logout'),
]


'''url(r'^$', 'new_pro.views.home'),
    
    url(r'^hello/$','artical.views.hello'),
    url(r'^hello_template/$','artical.views.hello_template'),
    url(r'^hello_template_simple/$','artical.views.hello_template_simple'),
    url(r'^hello_class_view/$',HelloTemplate.as_view()),'''
