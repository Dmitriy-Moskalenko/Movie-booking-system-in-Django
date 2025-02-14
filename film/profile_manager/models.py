from django.contrib.auth.models import User
from django.db import models

from film_app.models import Film, Sessions
from profile_manager.service import qrcode_create
from reservation.models import Hall


class Ticket(models.Model):
    """Таблица с билетами"""
    film = models.ForeignKey(Film, on_delete=models.CASCADE, blank=False, verbose_name='Фильм')
    seat = models.IntegerField(blank=False, verbose_name='Посадочное места')
    row = models.IntegerField(blank=False, verbose_name='Ряд')
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE, verbose_name='Сеанс')
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT, verbose_name='Зал')
    price = models.IntegerField(blank=False, verbose_name='Стоимость билета')
    qr_code = models.ImageField(blank=True, null=True, verbose_name='QR код')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')

    def save(self, *args, **kwargs):
        # Данные которые будут в qr коде
        data = {
            'Фильм': self.film.title,
            'Время сеанса': self.session.time,
            'Дата сеанса': self.session.date,
            'Зал': self.hall.pk,
            'Ряд': self.row,
            'Место': self.seat,
            'Стоимость билета': self.price,
        }

        if not self.qr_code:
            self.qr_code = qrcode_create(data)
        super().save(*args, **kwargs)

