from django.urls import path

from reservation import views


urlpatterns = [
    path('hall/<int:hall_id>/<int:session_id>/', views.hall, name='hall'),

]
