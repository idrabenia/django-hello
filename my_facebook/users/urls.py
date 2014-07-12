from django.conf.urls import patterns, include, url
from users import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<user_id>\d+)$', views.user_details, name='details'),
    url(r'^new$', views.user_form, name='user_form')
)

