from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
# from dirtyfields import DirtyFieldsMixin
from django.utils import timezone
from datetime import timedelta
from rest_framework.authtoken.models import Token



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',
                                verbose_name=_('User'))
    photo = models.ImageField(upload_to='profile/', blank=True, null=True, verbose_name=_('Photo'))
    
    def __str__(self) -> str:
        return self.user.username


class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    members = models.ManyToManyField(User, related_name='teams', verbose_name=_('Members'))
    score = models.IntegerField(default=0, verbose_name=_('Score'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    
    def __str__(self) -> str:
        return self.name
