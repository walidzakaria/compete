# Generated by Django 5.1.4 on 2025-02-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_otherquestion_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='page',
            field=models.CharField(blank=True, choices=[('', 'Home'), ('teams', 'Teams'), ('wheel', 'Wheel'), ('question', 'Question'), ('result', 'Result'), ('section', 'Section'), ('categories', 'Categories')], max_length=10, verbose_name='Page'),
        ),
    ]
