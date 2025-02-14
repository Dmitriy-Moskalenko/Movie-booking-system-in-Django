from django.db import models


class Hall(models.Model):
    """Таблица с залами"""
    seats = models.IntegerField(blank=False, verbose_name='Количество посадочных мест в одном ряду')
    rows = models.IntegerField(blank=False, verbose_name='Количество рядов')

