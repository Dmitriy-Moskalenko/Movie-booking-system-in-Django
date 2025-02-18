from django.shortcuts import render

from film_app.forms import SearchForm
from film_app.models import Film


def main_page(request):
    """Главная страница"""
    return render(request, 'main_page.html', {
        'form_search': SearchForm(request.GET)
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
