from django.db import models

from film_app.validators import *


status_people = (
            ('Режиссёр', 'Режиссёр'),
            ('Актёр', 'Актёр'),
            ('Продюсер', 'Продюсер'),
            ('Режиссер дубляжа', 'Режиссер дубляжа'),
            ('Переводчик', 'Переводчик'),
            ('Актер дубляжа', 'Актер дубляжа'),
            ('Сценарист', 'Сценарист'),
            ('Оператор', 'Оператор'),
            ('Композитор', 'Композитор'),
            ('Художник', 'Художник'),
            ('Монтажер', 'Монтажер'),
    )


class Film(models.Model):
    """Таблица с фильмами"""
    title = models.CharField(max_length=50, db_index=True, blank=False, verbose_name='Название фильма')
    slug = models.SlugField(unique=True, blank=False, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('Category', blank=False, on_delete=models.CASCADE, verbose_name='Категория')
    photo = models.ImageField(upload_to='film_photo/%Y/%m/%d/', blank=False,
                              validators=[photo_resolution_validator], verbose_name='Постер')
    video = models.FileField(upload_to='film_video/%Y/%m/%d/', blank=True, verbose_name='Трейлер')
    description = models.TextField(blank=False, verbose_name='Описание')
    year = models.IntegerField(blank=False, validators=[year_of_film_release_validator], verbose_name='Год выпуска')
    actor = models.ForeignKey('People', on_delete=models.CASCADE, verbose_name='Актёры')


class People(models.Model):
    """Таблица с людьми"""
    status = models.CharField(choices=status_people, blank=False, max_length=50, verbose_name='Статус')
    name = models.CharField(max_length=50, db_index=True, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=50, db_index=True, blank=False, verbose_name='Фамилия')
    slug = models.SlugField(unique=True, blank=False, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='people_photo/%Y/%m/%d/', blank=False,
                              validators=[photo_actor_resolution_validator], verbose_name='Фото')
    biography = models.TextField(blank=False, verbose_name='Биография')


class Category(models.Model):
    """Таблица с категориями"""
    title = models.CharField(max_length=50, blank=False, verbose_name='Категория')
    slug = models.SlugField(unique=True, blank=False, db_index=True, verbose_name='URL')
