from django.contrib import admin

from reviews.models import Title, Genre, Category


class ApiAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    search_fields = ('description',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Title, ApiAdmin)
admin.site.register(Genre)
admin.site.register(Category)
