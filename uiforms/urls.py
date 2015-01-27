from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^(?P<form_id>\d*)/$', views.render_form, name='render_form'),
)
