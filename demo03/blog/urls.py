from django.conf.urls import url
from .views import IndexView, SingleView
app_name = 'blog'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^single/(\d+)/$', SingleView.as_view(), name='single'),
]