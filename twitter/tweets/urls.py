# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$', views.TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.TweetUpdateView.as_view(), name='update'),
    url(r'^list/$', views.TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/delete/$', views.TweetDeleteView.as_view(), name='delete'),
    url(r'^api/$', views.TweetAPIView.as_view(), name='api'),
]
