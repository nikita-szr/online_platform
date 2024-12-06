from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator
from .permissions import IsOwnerOrModerator
from rest_framework.exceptions import PermissionDenied


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name='moderators').exists():
            raise PermissionDenied("Модераторы не имеют права создавать курсы.")
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrModerator]

    def perform_create(self, serializer):
        if self.request.user.groups.filter(name='moderators').exists():
            raise PermissionDenied("Модераторы не имеют права создавать уроки.")
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)