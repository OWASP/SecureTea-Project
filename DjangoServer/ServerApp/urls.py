from django.conf.urls import url
from django.urls.resolvers import URLPattern 
from ServerApp import views

urlpatterns = {
    url(r'check/$', views.test_api),
    url(r'notifs/$', views.notifs),
    url(r'uptime/$', views.get_uptime),
    url(r'processor/$', views.get_processor),
    url(r'cpu/$', views.get_cpu),
    url(r'username/$', views.get_username),
    url(r'ram/$', views.get_ram),
    url(r'swap/$', views.get_swap),
    url(r'hdd/$', views.get_hdd),
    url(r'process/$', views.process),
    url(r'diskio/$', views.get_diskio),
    url(r'netio/$', views.get_netio),
    url(r'status/$', views.check_status),
    url(r'stop/$', views.stop),
    url(r'login/$', views.get_login),
    url(r'sleep/$', views.sleep),

}