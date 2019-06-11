"""应用路由"""
from django.conf.urls import url
from .views import index, detail, result, login

app_name = 'vote'

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^result/(\d+)/$', result, name='result'),
    url(r"^login/$", login, name='login')
]
