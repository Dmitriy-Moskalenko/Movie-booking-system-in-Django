
def free_space(model, hall, session):
    """Функция, которая выводит все забронированные билеты в этом зале"""
    return model.objects.filter(hall=hall, session=session)

