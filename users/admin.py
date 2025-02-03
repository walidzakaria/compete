from django.contrib import admin
from .models import UserProfile, Team

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'score')
    filter_horizontal = ('members', )
    search_fields = ('name', )
    list_filter = ('score', )
    ordering = ('name', )
    # readonly_fields = ('score', )
    actions = ['reset_score']

    def reset_score(self, request, queryset):
        queryset.update(score=0)
        self.message_user(request, 'Score reset successfully')
    reset_score.short_description = 'Reset score'

