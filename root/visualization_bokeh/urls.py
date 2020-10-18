from django.urls import path

from . import views

app_name = 'visualization_bokeh'
urlpatterns = [
    path('vanilla', views.example, name='bokeh_vanilla'),
    path('ipywidget', views.example, name='bokeh_ipywidget'),
    path('panel', views.example, name='bokeh_panel'),
]
