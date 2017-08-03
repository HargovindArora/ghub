# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import views
# Create your views here.
from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contact/', views.contact, name = 'contact'),

]
