from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import StudentViewSet, SubjectViewSet, GradeViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = router.urls
