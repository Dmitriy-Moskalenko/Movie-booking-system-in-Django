from django.urls import path
from film_app import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search/', views.search, name='search'),
    path('film/<slug:film_slug>/', views.show_film, name='show_film'),
    path('sessions/<slug:film_slug>/', views.sessions_for_the_film, name='sessions_for_the_film'),
]
