from django.contrib.auth.models import User
from django.db import models

from film_app.models import Film
from profile_manager.service import qrcode_create


class Ticket(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, blank=False, verbose_name='Фильм')
    session_time = models.TimeField(blank=False, verbose_name='Время сеанса')
    hall_number = models.IntegerField(blank=False, verbose_name='Номер зала')
    seat_number = models.IntegerField(blank=False, verbose_name='Номер места')
    price = models.IntegerField(blank=False, verbose_name='Стоимость билета')
    qr_code = models.ImageField(blank=True, null=True, verbose_name='QR код')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def save(self, *args, **kwargs):
        data = {
            'Фильм': self.film.title,
            'Время сеанса': self.session_time,
            'Номер зала': self.hall_number,
            'Номер места': self.seat_number,
            'Стоимость билета': self.price,
        }

        if not self.qr_code:
            self.qr_code = qrcode_create(data)
        super().save(*args, **kwargs)


