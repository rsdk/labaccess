# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from labaccess import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<labor_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<labor_id>\d+)/anfrage/$', views.anfrage, name='anfrage'),
    url(r'^(?P<labor_id>\d+)/genehmigung/$', views.genehmigung, name='genehmigung'),
    url(r'^approve/$', views.approve, name='approve'),
    url(r'^approved/$', views.approved, name='approved'),
    url(r'^mail/$', views.mail, name='mail'),
    )