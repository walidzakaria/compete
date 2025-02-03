from rest_framework import serializers
from .models import (
    GeneralQuestion, PenaltyQuestion, PressureQuestion, WheelCategories, WheelQuestion, OtherQuestion,
    Process,
)


class GeneralQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralQuestion
        fields = '__all__'


class PenaltyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenaltyQuestion
        fields = '__all__'


class PressureQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureQuestion
        fields = '__all__'



class WheelCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelCategories
        fields = '__all__'


class WheelQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelQuestion
        fields = '__all__'


class OtherQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherQuestion
        fields = '__all__'


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'
