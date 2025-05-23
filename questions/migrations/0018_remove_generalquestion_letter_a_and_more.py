# Generated by Django 5.1.4 on 2025-02-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_delete_sortquestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalquestion',
            name='letter_a',
        ),
        migrations.RemoveField(
            model_name='generalquestion',
            name='letter_b',
        ),
        migrations.RemoveField(
            model_name='otherquestion',
            name='answered_a',
        ),
        migrations.RemoveField(
            model_name='otherquestion',
            name='answered_b',
        ),
        migrations.RemoveField(
            model_name='penaltyquestion',
            name='letter',
        ),
        migrations.RemoveField(
            model_name='pressurequestion',
            name='answered_a',
        ),
        migrations.RemoveField(
            model_name='pressurequestion',
            name='answered_b',
        ),
        migrations.RemoveField(
            model_name='wheelquestion',
            name='letter',
        ),
        migrations.AddField(
            model_name='process',
            name='answer',
            field=models.CharField(default='', max_length=255, verbose_name='Answer A'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='process',
            name='choices_a',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices A'),
        ),
        migrations.AddField(
            model_name='process',
            name='choices_b',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices B'),
        ),
        migrations.AddField(
            model_name='process',
            name='choices_c',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices C'),
        ),
        migrations.AddField(
            model_name='process',
            name='choices_d',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices D'),
        ),
        migrations.AddField(
            model_name='process',
            name='question',
            field=models.CharField(default='', max_length=255, verbose_name='Question A'),
            preserve_default=False,
        ),
    ]
