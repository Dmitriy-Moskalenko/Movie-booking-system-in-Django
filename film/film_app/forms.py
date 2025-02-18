from django import forms


class SearchForm(forms.Form):
    """Форма для поиска по сайту"""
    search = forms.CharField(required=False, label='',
                             widget=forms.TextInput(attrs={'class': 'search-form'}))