from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfile, Team


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'photo', )


class UserProfileDetailedSerializer(serializers.ModelSerializer):
    groups = UserGroupsSerializer(many=True)
    profile = UserProfileSerializer()
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'groups',
                  'profile', 'is_active', 'is_staff', 'is_superuser')


class UserListSerializer(serializers.ModelSerializer):
    
    photo = serializers.ImageField(source='profile.photo', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'photo', )


class TeamSerializer(serializers.ModelSerializer):
    members = UserListSerializer(many=True)
    class Meta:
        model = Team
        fields = '__all__'
