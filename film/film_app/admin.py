from django.contrib import admin

from film_app.models import *



admin.site.register(Category)


class SessionsAdminInline(admin.TabularInline):
    model = Sessions
    extra = 1


class PhotosFilmAdminInline(admin.TabularInline):
    model = PhotosFilm
    extra = 1


class PeopleAdminInline(admin.TabularInline):
    model = People
    extra = 1


class FilmAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cat']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['cat']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PhotosFilmAdminInline, PeopleAdminInline, SessionsAdminInline]


admin.site.register(PhotosFilm)
admin.site.register(People)
admin.site.register(Film, FilmAdmin)
admin.site.register(Sessions)
