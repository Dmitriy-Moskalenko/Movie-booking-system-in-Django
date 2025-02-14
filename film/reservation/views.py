from django.shortcuts import render, get_object_or_404, redirect

from film_app.models import Sessions
from profile_manager.forms import TicketForm
from profile_manager.models import Ticket
from reservation.models import Hall
from reservation.service import free_space


def hall(request, hall_id, session_id):
    """Страница с залом"""
    hall_model = get_object_or_404(Hall, pk=hall_id)
    session_model = get_object_or_404(Sessions, pk=session_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data_form = form.save(commit=False)
            data_form.user = request.user
            data_form.hall = hall_model
            data_form.session = session_model
            data_form.price = session_model.price
            data_form.film = session_model.film
            data_form.save()
            return redirect(request.path)
    else:
        form = TicketForm(request.POST)

    context = {
        'hall': hall_model,
        'rows': range(1, hall_model.rows + 1),
        'seats': range(1, hall_model.seats + 1),
        'free_space': free_space(Ticket, hall_model),
        'form': form,
    }
    return render(request, 'hall.html', context=context)