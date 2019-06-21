from django.conf.urls import url
from .views import blog, single, index, about, care, contact, comment, email, skip

app_name = 'pet'

urlpatterns = [
    url(r'^single/(\d+)/$', single, name='single'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^care/$', care, name='care'),
    url(r'^picture/$', care, name='picture'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^comment/(\d+)/$', comment, name='comment'),
    url(r'^send_email/$', email, name='send_email'),
    url(r'^skip/$', skip, name='skip'),
]
