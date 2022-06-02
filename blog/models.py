from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


def datetime_():
    return datetime.now() + timedelta(days=1)


class Note(models.Model):

    class Status(models.IntegerChoices):
        ACTIVE = 0, _('Активно')
        POSTONED = 1, _('Отложено')
        DONE = 2, _('Выполнено')

    title = models.CharField(max_length=300, verbose_name=_('Текст заметки'))
    important = models.BooleanField(default=False, verbose_name=_('Важно'))
    public = models.BooleanField(default=False, verbose_name=_('Публичная'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    deadline = models.DateField(default=datetime_, verbose_name=_('Выполнить до'))
    status = models.IntegerField(default=Status.ACTIVE, choices=Status.choices, verbose_name=_('Статус'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"Заметка №{self.id}"

    class Meta:
        verbose_name = _("Заметка")
        verbose_name_plural = _("Заметки")
        ordering = ['-create_at', '-important']
