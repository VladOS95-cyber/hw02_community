from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author')
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    # это свойство сработает для всех колонок: где пусто - там будет эта строка
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    '''Регистрация группы в админке'''

    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    empty_value_display = '-пусто-'


# регистрируем модели Post и Group
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
