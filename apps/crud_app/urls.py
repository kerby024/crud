from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/user$', views.users),
    # url(r'^$', views.editusers),
    # url(r'^$', views.newusers)
]