# Generated by Django 5.1.5 on 2025-01-27 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='page',
            field=models.CharField(choices=[('teams', 'Teams'), ('wheel', 'Wheel'), ('question', 'Question'), ('result', 'Result'), ('section', 'Section')], max_length=10, verbose_name='Page'),
        ),
    ]
