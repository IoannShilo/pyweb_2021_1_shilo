# Generated by Django 4.0.4 on 2022-06-04 09:12

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_note_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-create_at', '-important'], 'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
        migrations.RemoveField(
            model_name='note',
            name='message',
        ),
        migrations.RemoveField(
            model_name='note',
            name='update_at',
        ),
        migrations.AddField(
            model_name='note',
            name='deadline',
            field=models.DateField(default=blog.models.datetime_, verbose_name='Выполнить до'),
        ),
        migrations.AddField(
            model_name='note',
            name='important',
            field=models.BooleanField(default=False, verbose_name='Важно'),
        ),
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.IntegerField(choices=[(0, 'Активно'), (1, 'Отложено'), (2, 'Выполнено')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='note',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='note',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Публичная'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Текст заметки'),
        ),
    ]
