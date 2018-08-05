from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>[\w\-]+)$', views.profile),
    url(r'^profile/edit$', views.edit_profile, name='edit'),
]
