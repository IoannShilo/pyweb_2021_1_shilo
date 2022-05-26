from django.contrib import admin

from .models import Note

@admin.register(Note)  # связываем админку с моделью
class NoteAdmin(admin.ModelAdmin):
    # Поля в списке
    list_display = (
        'title', 'create_at', 'status', 'author', 'public', 'important'

    )
    # #
    # # # Группировка поля в режиме редактирования
    fields = (('title', 'public', 'important'), ('status', ), ('author', ), 'create_at')
    # Поля только для чтения в режиме редактирования
    readonly_fields = ('create_at', 'author')
    # #
    # Поиск по выбранным полям
    search_fields = ['title',]
    #
    # Фильтры справа
    list_filter = ('public', 'important', 'status')

    # # Widget для удобного поиска записей
    autocomplete_fields = ['author', ]  # todo для поиска по автору


    def admin_authors(self, instance):
        return ", ".join(author.username for author in instance.authors.all())

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset\
            .prefetch_related("author")\
            .order_by('-create_at', '-important')
