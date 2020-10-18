from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prefect_flow', views.prefect_flow, name='prefect_flow'),
    path('prefect_flow_run', views.prefect_flow_run, name='prefect_flow_run')
]
