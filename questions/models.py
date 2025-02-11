from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeneralQuestion(models.Model):
    question_a = models.CharField(max_length=255, verbose_name='Question A')
    choices_aa = models.CharField(max_length=255, verbose_name='Choices A', blank=True, null=True)
    choices_ab = models.CharField(max_length=255, verbose_name='Choices B', blank=True, null=True)
    choices_ac = models.CharField(max_length=255, verbose_name='Choices C', blank=True, null=True)
    choices_ad = models.CharField(max_length=255, verbose_name='Choices D', blank=True, null=True)
    answer_a = models.CharField(max_length=255, verbose_name='Answer A')
    
    question_b = models.CharField(max_length=255, verbose_name='Question B')
    choices_ba = models.CharField(max_length=255, verbose_name='Choices A', blank=True, null=True)
    choices_bb = models.CharField(max_length=255, verbose_name='Choices B', blank=True, null=True)
    choices_bc = models.CharField(max_length=255, verbose_name='Choices C', blank=True, null=True)
    choices_bd = models.CharField(max_length=255, verbose_name='Choices D', blank=True, null=True)
    answer_b = models.CharField(max_length=255, verbose_name='Answer B')
    
    duration = models.IntegerField(default=0, verbose_name='Duration')
    used = models.BooleanField(default=False, verbose_name='Used')
    
    def __str__(self):
        return f'{self.question_a}'


class PenaltyQuestion(models.Model):
    question = models.CharField(max_length=255, verbose_name='Question')
    choices_a = models.CharField(max_length=255, verbose_name='Choices A', blank=True, null=True)
    choices_b = models.CharField(max_length=255, verbose_name='Choices B', blank=True, null=True)
    choices_c = models.CharField(max_length=255, verbose_name='Choices C', blank=True, null=True)
    choices_d = models.CharField(max_length=255, verbose_name='Choices D', blank=True, null=True)
    answer = models.CharField(max_length=255, verbose_name='Answer')
    
    duration = models.IntegerField(default=0, verbose_name='Duration')
    used = models.BooleanField(default=False, verbose_name='Used')
    
    
    def __str__(self):
        return f'{self.id}'


class PressureQuestion(models.Model):
    question = models.CharField(max_length=255, verbose_name='Question')
    choices_a = models.CharField(max_length=255, verbose_name='Choices A', blank=True, null=True)
    choices_b = models.CharField(max_length=255, verbose_name='Choices B', blank=True, null=True)
    choices_c = models.CharField(max_length=255, verbose_name='Choices C', blank=True, null=True)
    choices_d = models.CharField(max_length=255, verbose_name='Choices D', blank=True, null=True)
    answer = models.CharField(max_length=255, verbose_name='Answer')
    
    used = models.BooleanField(default=False, verbose_name='Used')
    
    def __str__(self):
        return f'{self.id}'


class WheelCategories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    color = models.CharField(max_length=20, verbose_name='Color')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Wheel Categories'


class WheelQuestion(models.Model):
    question = models.CharField(max_length=255, verbose_name='Question')
    choices_a = models.CharField(max_length=255, verbose_name='Choices A', blank=True, null=True)
    choices_b = models.CharField(max_length=255, verbose_name='Choices B', blank=True, null=True)
    choices_c = models.CharField(max_length=255, verbose_name='Choices C', blank=True, null=True)
    choices_d = models.CharField(max_length=255, verbose_name='Choices D', blank=True, null=True)
    answer = models.CharField(max_length=255, verbose_name='Answer')
    category = models.ForeignKey(WheelCategories, on_delete=models.CASCADE, verbose_name='Category')
    
    duration = models.IntegerField(default=0, verbose_name='Duration')
    used = models.BooleanField(default=False, verbose_name='Used')
    
    def __str__(self):
        return f'{self.id}'


class OtherQuestion(models.Model):
    question = models.CharField(max_length=255, verbose_name='Question')
    duration = models.IntegerField(default=0, verbose_name='Duration')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.id}'


class Process(models.Model):
    
    class PageOptions(models.TextChoices):
        HOME = '', 'Home'
        TEAMS = 'teams', 'Teams'
        WHEEL = 'wheel', 'Wheel'
        QUESTION = 'question', 'Question'
        RESULT = 'result', 'Result'
        SECTION = 'section', 'Section'
        CATEGORIES = 'categories', 'Categories'
    
    class SectionOptions(models.TextChoices):
        GENERAL_QUESTIONS = 'أسئلة عامة', 'أسئلة عامة'
        PENALTIES = 'ضربات جزاء', 'ضربات جزاء'
        UNDER_PRESSURE = 'تحت الضغط', 'تحت الضغط'
        TALENTS = 'المواهب', 'المواهب'
        WHEEL = 'عجلة الحظ', 'عجلة الحظ'
    
    
    class CurrentTeamOptions(models.TextChoices):
        A = 'a', 'a'
        B = 'b', 'b'
    
    page = models.CharField(max_length=10, choices=PageOptions.choices, verbose_name='Page', blank=True)
    time_started = models.DateTimeField(blank=True, null=True)
    user_locked = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    section_title = models.CharField(max_length=200, blank=True, null=True, choices=SectionOptions.choices)
    question_index = models.SmallIntegerField(default=0, verbose_name='Question Index')
    selected_answer = models.SmallIntegerField(default=0, verbose_name='Selected Answer')
    interval_number = models.IntegerField(default=300, verbose_name='Interval Number')
    team_a_result = models.IntegerField(default=0)
    team_b_result = models.IntegerField(default=0)
    current_team = models.CharField(max_length=1, choices=CurrentTeamOptions, default=CurrentTeamOptions.A)
    penalty = models.CharField(max_length=300, blank=True, null=True)
    pressure_duration = models.IntegerField(default=60, verbose_name='Pressure Duration')
    
    question = models.CharField(max_length=255, verbose_name='Question', blank=True, null=True)
    choices_a = models.CharField(max_length=255, verbose_name='Choices A', blank=True, null=True)
    choices_b = models.CharField(max_length=255, verbose_name='Choices B', blank=True, null=True)
    choices_c = models.CharField(max_length=255, verbose_name='Choices C', blank=True, null=True)
    choices_d = models.CharField(max_length=255, verbose_name='Choices D', blank=True, null=True)
    answer = models.CharField(max_length=255, verbose_name='Answer', blank=True, null=True)
    duration = models.IntegerField(default=60, verbose_name='Duration')
    max_duration = models.IntegerField(default=60, verbose_name='Max Duration')
    paused = models.BooleanField(default=False, verbose_name='Paused')
    time_left = models.IntegerField(blank=True, null=True)
    
        
    def __str__(self):
        return self.page

    class Meta:
        verbose_name_plural = 'Processes'
