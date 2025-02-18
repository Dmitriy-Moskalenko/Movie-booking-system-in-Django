from django.urls import path
from film_app import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search/', views.search, name='search'),
]
