from django.shortcuts import render

from film_app.forms import SearchForm, SortedByCatForm, SortedByRatingForm
from film_app.models import Film, Category
from film_app.service import filters


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

