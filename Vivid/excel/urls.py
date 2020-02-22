from django.urls import path

from . import views

urlpatterns = [
    path('',views.index_excel,name='index_excel')
]
