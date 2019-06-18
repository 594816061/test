from django.conf.urls import url
from .feed import ArticleFeed
from .views import IndexView, SingleView, ArchiveView, CategoryView, TagView, EmailView
from haystack.views import SearchView
app_name = 'blog'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^single/(\d+)/$', SingleView.as_view(), name='single'),
    url(r'^archive/(\d+)/(\d+)/$', ArchiveView.as_view(), name='archive'),
    url(r'^category/(\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(\d+)/$', TagView.as_view(), name='tag'),
    url(r'^rss/$', ArticleFeed, name='rss'),
    url(r'^send_email/$', EmailView.as_view(), name='send_email'),
    url(r'^search/$', SearchView(), name='search'),
]