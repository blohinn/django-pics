from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.photo_feed, name='photo_feed'),
]