from django.contrib import admin
from django.urls import path, include

from film import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('film_app.urls')),
    path('', include('profile_manager.urls')),
    path('', include('reservation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)