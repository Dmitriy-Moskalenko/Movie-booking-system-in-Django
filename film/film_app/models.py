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
    title = models.CharField(max_length=50, db_index=True, blank=False, verbose_name='Название фильма')
    slug = models.SlugField(unique=True, blank=False, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='images_game/%Y/%m/%d/', blank=False,
                              validators=[photo_resolution_validator], verbose_name='Постер')
    description = models.TextField(blank=False, verbose_name='Описание')
    year = models.IntegerField(blank=False, validators=[year_of_film_release_validator], verbose_name='Год выпуска')
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE, verbose_name='Актёры')


class People(models.Model):
    status = models.CharField(choices=status_people, blank=False, validators='Статус')
    name = models.CharField(max_length=50, db_index=True, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=50, db_index=True, blank=False, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='images_game/%Y/%m/%d/', blank=False,
                              validators=[photo_actor_resolution_validator], verbose_name='Фото актёра')
    biography = models.TextField(blank=False, verbose_name='Биография')