# Generated by Django 5.1.4 on 2025-02-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0024_process_max_duration_process_paused_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='time_left',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
