from django.urls import path
from . import views

urlpatterns = [
    path('form_with_vue', views.author_books_formset, name='form_with_vue'),
    path('rest_get_request', views.rest_get_request, name='rest_get_request'),
    path('backtest_template', views.bt, name='backtest_template'),
]
