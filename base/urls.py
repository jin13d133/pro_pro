from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.shortcuts import render

urlpatterns= [
    url(r'^$', views.temp, name='temp'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^my_hash/$', views.my_hash, name='my_hash'),
    url(r'^create/$', views.create, name='create'),
    url(r'^virus_hash/$', views.virus_hash, name='virus_hash'),
    url(r'^about/$', views.about, name='about'),
]