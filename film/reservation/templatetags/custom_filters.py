from django import template

register = template.Library()


@register.simple_tag
def place_occupied(free_space, row, seat):
    """Проверяет, занято ли место"""
    for space in free_space:
        if space.row == row and space.seat == seat:
            return True  # True если место занято
    return False


