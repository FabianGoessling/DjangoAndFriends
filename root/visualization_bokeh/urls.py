from django.urls import path

from . import views

app_name = 'visualization_bokeh'
urlpatterns = [
    path('', views.example, name='visualization_bokeh'),
    path('ipywidget', views.example, name='ipywidget'),
    path('panel', views.example, name='panel'),
]
