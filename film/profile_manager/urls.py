from django.urls import path

from profile_manager import views


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
]
