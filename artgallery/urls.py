from django.conf.urls import url
from django.urls import URLPattern
from . import views

urlpatterns=[
    url(r'^$', views.artgallery, name='artgallery'),
]