# Generated by Django 5.0.6 on 2025-02-26 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='actor',
        ),
        migrations.AddField(
            model_name='people',
            name='film',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='film_app.film', verbose_name='Фильм'),
            preserve_default=False,
        ),
    ]
