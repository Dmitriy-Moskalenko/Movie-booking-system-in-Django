# Generated by Django 5.0.6 on 2025-02-15 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0005_sessions_hall'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessions',
            name='hall',
        ),
    ]
