from django import forms

from film_app.models import Category, Film


class SearchForm(forms.Form):
    """Форма для поиска по сайту"""
    search = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={'class': 'search-form'}))


class SortedByCatForm(forms.ModelForm):
    """Форма для сортировки по категории"""
    title = forms.ModelChoiceField(
        required=False,
        label='',
        empty_label='Все категории',
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={'class': 'category_sorted'}))

    class Meta:
        model = Category
        fields = ['title']


class SortedByRatingForm(forms.ModelForm):
    """Форма для сортировки по рейтингу"""
    grade = forms.IntegerField(
        required=False,
        label='',
        widget=forms.NumberInput(
            attrs={
                'class': 'rating_sorted', 'type': 'range',
                'min': 1, 'max': 5, 'id': 'rangeInput'
                   }))

    class Meta:
        model = Film
        fields = ['grade']