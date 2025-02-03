from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoObjectPermissions, AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view, permission_classes
from .serializers import (
    UserProfileDetailedSerializer,
    UserProfileSerializer, UserGroupsSerializer, ProfileSerializer, UserListSerializer,
    TeamSerializer,
)

from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserProfile, Team
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.cache import cache
from datetime import timedelta
from django.utils import timezone

# Create your views here.
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    
    def get(self, request):
        user = request.user
        serializer = UserProfileDetailedSerializer(user)
        return Response(serializer.data)


class UserProfileView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # save the user profile with the current user


class UserGroupsView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserGroupsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class TeamViewSet(ModelViewSet):
    
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return Team.objects.filter(active=True)
        return Team.objects.all()
