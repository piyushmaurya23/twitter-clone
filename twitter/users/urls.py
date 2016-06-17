# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^admin/$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),

    url(r'^address/create/$', views.UserAddressCreateView.as_view(), name='address_create'),
    url(r'^address/(?P<pk>\d+)/$', views.UserAddressDetailView.as_view(), name='address_detail'),
    url(r'^address/(?P<pk>\d+)/update/$', views.UserAddressUpdateView.as_view(), name='address_update'),
    url(r'^address/list/$', views.UserAddressListView.as_view(), name='address_list'),
    url(r'^address/(?P<pk>\d+)/delete/$', views.UserAddressDeleteView.as_view(), name='address_delete'),
    url(r'^address/api/$', views.UserAddressAPIView.as_view(), name='api'),
    url(r'^address/api/(?P<pk>\d+)/$', views.UserAddressPutAPIView.as_view(), name='put_api'),
]
