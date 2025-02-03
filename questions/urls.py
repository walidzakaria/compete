
from rest_framework import routers
from .views import (
    GeneralQuestionViewSet, PenaltyQuestionViewSet, PressureQuestionViewSet,
    WheelCategoriesViewSet, WheelQuestionViewSet, OtherQuestionViewSet, ProcessViewSet
)

router = routers.DefaultRouter()
router.register(r'general-questions', GeneralQuestionViewSet, basename='general-questions')
router.register(r'penalty-questions', PenaltyQuestionViewSet, basename='penalty-questions')
router.register(r'pressure-questions', PressureQuestionViewSet, basename='pressure-questions')
router.register(r'wheel-categories', WheelCategoriesViewSet, basename='wheel-categories')
router.register(r'wheel-questions', WheelQuestionViewSet, basename='wheel-questions')
router.register(r'other-questions', OtherQuestionViewSet, basename='other-questions')
router.register(r'process', ProcessViewSet, basename='process')


urlpatterns = router.urls
