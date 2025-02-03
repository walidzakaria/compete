from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    UserInfoView, TeamViewSet
)


urlpatterns = [
    path('user-info/', UserInfoView.as_view(), name='user-info'),
    path('team/', TeamViewSet.as_view({'get': 'list'}), name='team-list'),
]

