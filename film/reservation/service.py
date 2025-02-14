
def free_space(model, hall):
    """Функция, которая выводит все забронированные билеты в этом зале"""
    return model.objects.filter(hall=hall)

