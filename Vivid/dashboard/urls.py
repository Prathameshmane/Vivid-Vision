from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.base_dash, name='base_dash'),
]
