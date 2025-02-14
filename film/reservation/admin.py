from django.contrib import admin

from film_app.models import Sessions
from reservation.models import Hall

admin.site.register(Hall)
admin.site.register(Sessions)
