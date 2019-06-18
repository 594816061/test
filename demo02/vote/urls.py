"""应用路由"""
from django.conf.urls import url
from .views import index, detail, result, login, regist, my_logout, check_my_username, my_active, verify
app_name = 'vote'

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^result/(\d+)/$', result, name='result'),
    url(r"^login/$", login, name='login'),
    url(r'^regist/$', regist, name='regist'),
    url(r'^my_logout/$', my_logout, name='my_logout'),
    url(r'^check_my_username/$', check_my_username, name='check_my_username'),
    url(r'^my_active/(.*?)/$', my_active, name='my_active'),
    url(r'^verify/$', verify, name='verify'),
]
