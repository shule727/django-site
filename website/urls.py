from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about-us$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^publications/(?P<publication_id>[0-9]+)$', views.post, name='post'),
    url(r'^confirmation$', views.confirmation, name='confirmation'),
]
