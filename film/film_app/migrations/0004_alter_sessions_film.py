# Generated by Django 5.0.6 on 2025-02-09 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0003_sessions_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessions',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film_app.film', verbose_name='Фильм'),
        ),
    ]
