from django.conf.urls import url
from django.urls.resolvers import URLPattern
from ApiApp import views

urlpatterns = [
    url(r'^meta/$', views.get_meta),
    url(r'^module_meta/$', views.get_module_meta),
    url(r'^cmd/$', views.run_cmd),
]