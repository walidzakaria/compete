# Generated by Django 5.1.5 on 2025-01-31 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
