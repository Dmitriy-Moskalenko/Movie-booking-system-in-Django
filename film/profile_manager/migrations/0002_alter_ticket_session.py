# Generated by Django 5.0.6 on 2025-02-15 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0005_sessions_hall'),
        ('profile_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film_app.sessions', verbose_name='Сеанс'),
        ),
    ]
