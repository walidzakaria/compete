from django.contrib import admin

from .models import (
    GeneralQuestion, PenaltyQuestion, PressureQuestion, WheelCategories, WheelQuestion, OtherQuestion,
    Process,
)

# Register your models here.
@admin.register(GeneralQuestion)
class GeneralQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_a', 'answer_a', 'question_b', 'answer_b', 'duration', 'used', )
    list_filter = ('used', )
    
    actions = ['mark_unused']
    
    def mark_unused(self, request, queryset):
        queryset.update(used=False)
    mark_unused.short_description = 'Mark selected as unused'
    

@admin.register(PenaltyQuestion)
class PenaltyQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'choices_a', 'choices_b', 'choices_c', 'choices_d', 'answer', 'duration', 'used')
    list_filter = ('used', )
    
    actions = ['mark_unused']
    
    def mark_unused(self, request, queryset):
        queryset.update(used=False)
    mark_unused.short_description = 'Mark selected as unused'
    

@admin.register(PressureQuestion)
class PressureQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'choices_a', 'choices_b', 'choices_c', 'choices_d', 'answer', 'used')
    list_filter = ('used', )

    actions = ['mark_unused']
    
    def mark_unused(self, request, queryset):
        queryset.update(used=False)
    mark_unused.short_description = 'Mark selected as unused'
    

@admin.register(WheelCategories)
class WheelCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', )


@admin.register(WheelQuestion)
class WheelQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'choices_a', 'choices_b', 'choices_c', 'choices_d', 'answer', 'duration', 'used')
    list_filter = ('used', )
    
    actions = ['mark_unused']
    
    def mark_unused(self, request, queryset):
        queryset.update(used=False)
    mark_unused.short_description = 'Mark selected as unused'
    

@admin.register(OtherQuestion)
class OtherQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'duration', 'active', )


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('page', 'time_started', 'user_locked', 'team_a_result', 'team_b_result', )
