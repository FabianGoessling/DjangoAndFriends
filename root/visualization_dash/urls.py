from django.urls import path
from django.conf.urls import url
from . import views
from . import dashboard  # REQUIRED?
from django.views.generic import TemplateView

app_name = 'visualization_dash'
urlpatterns = [
    path('', TemplateView.as_view(template_name='visualization_dash/index.html')),
    path('welcome/', views.home, name='welcome'),
]
