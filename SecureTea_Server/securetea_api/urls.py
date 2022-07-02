from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_api),
    path('userlogin/', views.login),
    path('register/', views.register),

    path('uptime/', views.get_uptime),
    path('processor/', views.get_processor),
    path('cpu/', views.get_cpu),
    path('username/', views.get_username),
    path('ram/', views.get_ram),
    path('swap/', views.get_swap),
    path('hdd/', views.get_hdd),
    path('process/', views.get_process),
    path('diskio/', views.get_diskio),
    path('netio/', views.get_networks),
    path('status/', views.check_status),
    path('login/', views.get_login),
    path('stop/', views.stop),
    path('sleep/', views.sleep),

]
