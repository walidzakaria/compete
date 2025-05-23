# Generated by Django 5.1.5 on 2025-01-25 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_a', models.CharField(max_length=255, verbose_name='Question A')),
                ('choices_aa', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices A')),
                ('choices_ab', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices B')),
                ('choices_ac', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices C')),
                ('choices_ad', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices D')),
                ('answer_a', models.CharField(max_length=255, verbose_name='Answer A')),
                ('letter_a', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=1, null=True)),
                ('question_b', models.CharField(max_length=255, verbose_name='Question B')),
                ('choices_ba', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices A')),
                ('choices_bb', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices B')),
                ('choices_bc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices C')),
                ('choices_bd', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices D')),
                ('answer_b', models.CharField(max_length=255, verbose_name='Answer B')),
                ('letter_b', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=1, null=True)),
                ('duration', models.IntegerField(default=0, verbose_name='Duration')),
            ],
        ),
        migrations.CreateModel(
            name='OtherQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('answered_a', models.BooleanField(default=False, verbose_name='Answered A')),
                ('answered_b', models.BooleanField(default=False, verbose_name='Answered B')),
            ],
        ),
        migrations.CreateModel(
            name='PenaltyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('choices_a', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices A')),
                ('choices_b', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices B')),
                ('choices_c', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices C')),
                ('choices_d', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices D')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('letter', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PressureQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('choices_a', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices A')),
                ('choices_b', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices B')),
                ('choices_c', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices C')),
                ('choices_d', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices D')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('answered_a', models.BooleanField(default=False, verbose_name='Answered A')),
                ('answered_b', models.BooleanField(default=False, verbose_name='Answered B')),
            ],
        ),
        migrations.CreateModel(
            name='SortQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('letter', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WheelCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='WheelQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Question')),
                ('choices_a', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices A')),
                ('choices_b', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices B')),
                ('choices_c', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices C')),
                ('choices_d', models.CharField(blank=True, max_length=255, null=True, verbose_name='Choices D')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
                ('letter', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=1, null=True)),
                ('used', models.BooleanField(default=False, verbose_name='Used')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.wheelcategories', verbose_name='Category')),
            ],
        ),
    ]
