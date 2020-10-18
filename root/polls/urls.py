
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('colors/', views.myview, name='vote'),
    path('create_book_normal/', views.create_book_normal, name='create_book_normal'),
    path('create_model', views.create_book_model_form, name='create_book_model_form'),
    path('create_with_author', views.create_book_with_authors, name='create_book_with_authors'),
]
