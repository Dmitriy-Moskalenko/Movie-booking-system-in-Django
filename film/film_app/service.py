def filters(request, model, form_cat):
    """Функция со всеми сортировками"""
    if request.method == 'GET':
        if request.GET.get('cat_select_id') == 'CatSelect':
            return sorted_by_category(request, model, form_cat)
        elif request.GET.get('grade_id') == 'Grade':
            return sort_by_rating(request, model, form_cat)
        elif request.GET.get('asc_desc_id') == 'AscDesc':
            return sort_by_year(request, model)


def sorted_by_category(request, model, form_cat):
    """Функция, которая сортирует фильмы по категории"""
    form = form_cat[0](request.GET)
    if form.is_valid():
        form_ = form.cleaned_data['title']
        return model.objects.filter(cat=form_)


def sort_by_rating(request, model, form_cat):
    """Функция, которая сортирует фильмы по рейтингу"""
    form = form_cat[1](request.GET)
    if form.is_valid():
        form_ = form.cleaned_data['grade']
        return model.objects.filter(grade=form_)


def sort_by_year(request, model):
    """Функция, которая сортирует фильмы по году выхода"""
    query = request.GET.get('sort')
    if query == 'asc':
        print('asc')
        return model.objects.all().order_by('year')
    elif query == 'desc':
        print('desc')
        return model.objects.all().order_by('-year')


