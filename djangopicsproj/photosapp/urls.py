from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.photo_feed, name='photo_feed'),
    url(r'^photo/upload', views.upload_photo, name='upload_photo')
]