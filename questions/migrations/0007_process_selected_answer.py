# Generated by Django 5.1.5 on 2025-01-28 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_alter_process_user_locked'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='selected_answer',
            field=models.SmallIntegerField(default=0, verbose_name='Selected Answer'),
        ),
    ]
