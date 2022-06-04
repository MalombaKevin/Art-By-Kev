from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('', views.artgallery, name='artgallery'),
    path('^artview/', views.artview, name='artview'),
    path('search/', views.search_results, name='search_results'),
    path('locations/', views.location_search, name='locations'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)