from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from datetime import date


def photo_resolution_validator(photo):
    """Проверка разрешения постера
    Максимальное разрешение постера - 2000х2800
    Минимальное разрешение постера - 200х300
    """
    width, height = get_image_dimensions(photo)
    max_width, min_width = 2000, 200
    max_height, min_height = 2800, 300

    if width > max_width or height > max_height:
        raise ValidationError(f'Максимальное разрешение изображения {max_width}x{max_height}')

    if width < min_width or height < min_height:
        raise ValidationError(f'Минимальное разрешение изображения {min_width}x{min_height}')


def year_of_film_release_validator(year):
    """Проверка года выпуска фильма
    Год фильма не должен превышать текущий год
    """
    if year > date.today().year:
        raise ValidationError(f'Год фильма больше текущего года')


def photo_actor_resolution_validator(photo):
    """Проверка разрешения фотографии актёра
    Максимальное разрешение постера - 1000х1250
    Минимальное разрешение постера - 750х1000
    """
    width, height = get_image_dimensions(photo)
    max_width, min_width = 1000, 750
    max_height, min_height = 1250, 1000

    if width > max_width or height > max_height:
        raise ValidationError(f'Максимальное разрешение фотографии {max_width}x{max_height}')

    if width < min_width or height < min_height:
        raise ValidationError(f'Минимальное разрешение фотографии {min_width}x{min_height}')


def photo_for_film_validator(photo):
    """Проверка разрешения фотографии актёра
    Максимальное разрешение постера - 1000х1250
    Минимальное разрешение постера - 750х1000
    """
    width, height = get_image_dimensions(photo)
    max_width, min_width = 2560, 1280
    max_height, min_height = 1440, 720

    if width > max_width or height > max_height:
        raise ValidationError(f'Максимальное разрешение фотографии {max_width}x{max_height}')

    if width < min_width or height < min_height:
        raise ValidationError(f'Минимальное разрешение фотографии {min_width}x{min_height}')