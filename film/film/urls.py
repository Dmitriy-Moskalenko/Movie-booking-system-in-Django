from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film_app.urls')),
    path('', include('profile_manager.urls')),
]
