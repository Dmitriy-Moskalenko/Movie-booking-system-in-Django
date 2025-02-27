from django.shortcuts import render, get_object_or_404

from film_app.forms import SearchForm, SortedByCatForm, SortedByRatingForm
from film_app.models import Film, Category, Sessions, People, PhotosFilm
from film_app.service import filters
from film_app.models import Hall


def main_page(request):
    """Главная страница"""
    filters_ = filters(request, Film, (SortedByCatForm, SortedByRatingForm))

    return render(request, 'main_page.html', {
        'form_search': SearchForm(request.GET),
        'all_film': filters_ if filters_ else Film.objects.all(),
        'category_form': SortedByCatForm(request.GET),
        'grade_form': SortedByRatingForm(request.GET),

    })


def search(request):
    """Поиск по сайту"""
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            form_data = form.cleaned_data['search']
            models = Film.objects.filter(title__icontains=form_data)
            return render(request, 'search.html', {'models': models})
    else:
        form = SearchForm(request.GET)
    return render(request, 'search.html', {'form_search': form})


def show_film(request, film_slug):
    """Страница с фильмом"""
    film = get_object_or_404(Film, slug=film_slug)
    peoples = People.objects.filter(film__slug=film_slug)
    photos_film = PhotosFilm.objects.filter(film__slug=film_slug)

    return render(request, 'show_film.html', {
        'film': film,
        'peoples': peoples,
        'photos': photos_film,
    })


def sessions_for_the_film(request, film_slug):
    """Страница с выбором сеанса и зала"""
    sessions = Sessions.objects.filter(film__slug=film_slug)
    halls = Hall.objects.filter(film__slug=film_slug)
    return render(request, 'sessions_for_the_film.html', {
        'sessions': sessions,
        'halls': halls,
    })