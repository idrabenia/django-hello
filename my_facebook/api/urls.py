from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^$', views.api_root),
    url(r'^user$', views.UserList.as_view(), name="user-list"),
    url(r'^user/(?P<pk>\d+)$', views.UserDetails.as_view(), name="user-detail"),
    url(r'^group$', views.GroupList.as_view(), name="group-list"),
    url(r'^group/(?P<pk>\d+)$', views.GroupDetails.as_view(), name="group-detail")
)
