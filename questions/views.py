from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from .models import (
    GeneralQuestion, PenaltyQuestion, PressureQuestion, WheelCategories, WheelQuestion, OtherQuestion,
    Process,
)
from .serializers import (
    GeneralQuestionSerializer, PenaltyQuestionSerializer, PressureQuestionSerializer,
    WheelCategoriesSerializer, WheelQuestionSerializer, OtherQuestionSerializer, ProcessSerializer,
)
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoObjectPermissions, AllowAny

# Create your views here.
class GeneralQuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GeneralQuestionSerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return GeneralQuestion.objects.filter(used=False)
        return GeneralQuestion.objects.all()
    
    @action(detail=False, methods=['get'])
    def next_question(self, request):
        questions = self.get_queryset().order_by('id')
        for question in questions:
            if not question.used:
                return Response(self.get_serializer(question).data)
        return Response(status=status.HTTP_404_NOT_FOUND)
        


class PenaltyQuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PenaltyQuestionSerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return PenaltyQuestion.objects.filter(used=False)
        return PenaltyQuestion.objects.all()

    @action(detail=False, methods=['get'])
    def next_question(self, request):
        questions = self.get_queryset().order_by('id')
        for question in questions:
            if not question.used:
                return Response(self.get_serializer(question).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class PressureQuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PressureQuestionSerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return PressureQuestion.objects.filter(used=False)
        return PressureQuestion.objects.all()
    
    @action(detail=False, methods=['get'])
    def next_question(self, request):
        questions = self.get_queryset().order_by('id')
        for question in questions:
            if not question.used:
                return Response(self.get_serializer(question).data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class WheelCategoriesViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WheelCategories.objects.all()
    serializer_class = WheelCategoriesSerializer


class WheelQuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WheelQuestion.objects.all()
    serializer_class = WheelQuestionSerializer
    
    @action(detail=False, methods=['get'])
    def next_question(self, request):
        category = request.query_params.get('category')
        question = self.get_queryset().filter(category=category, used=False).first()
        print('cat', category, 'ques', question)
        if question:
            question.used = True
            question.save()
            return Response(self.get_serializer(question).data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class OtherQuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OtherQuestionSerializer
    
    def get_queryset(self):
        if self.action == 'list':
            return OtherQuestion.objects.filter(active=True).all()
        return OtherQuestion.objects.all()


class ProcessViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    
    @action(detail=False, methods=['get'])
    def lock_process(self, request):
        try:
            process_instance = Process.objects.get(pk=1)
        except Process.DoesNotExist:
            return Response({"error": "Process not found"}, status=status.HTTP_404_NOT_FOUND)

        if process_instance.user_locked:
            return Response({"error": "Process already locked", "locked_by": process_instance.user_locked.pk},
                            status=status.HTTP_400_BAD_REQUEST)

        process_instance.user_locked = request.user
        process_instance.interval_number = 1000
        process_instance.save()
        return Response({"message": "Process successfully locked", "locked_by": request.user.pk}, status=status.HTTP_200_OK)
 