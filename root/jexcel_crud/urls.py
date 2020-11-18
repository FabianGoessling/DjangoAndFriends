from django.urls import path

from . import views

urlpatterns = [
    path('', views.jexcel_input(), name='jexcel_page'),
    path('forms', views.dynamic_form(), name='forms')
]