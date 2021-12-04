from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    url(r'^$', views.showmap),
]