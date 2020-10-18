from django.urls import path

from . import views

urlpatterns = [
    path('', views.message_tester, name='message_test'),
]
