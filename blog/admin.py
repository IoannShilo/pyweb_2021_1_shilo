from django.contrib import admin

from blog.models import Note


@admin.register(Note)
class Admin(admin.ModelAdmin):
    pass
