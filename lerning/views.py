# flake8: noqa

from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from lerning.models import Course, Lesson, Subscription
from lerning.pagination import CustomPagination
from lerning.serializers import (CourseSerializer, LessonSerializer,)
from users.permissions import IsModer, IsOwner


class CourseViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_permissions(self):
        if self.action == [
            "create",
        ]:
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == [
            "destroy",
        ]:
            self.permission_classes = (IsOwner | ~IsModer,)
        return super().get_permissions()


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)
    pagination_class = CustomPagination


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModer | IsOwner)


class SubscriptionApiView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        course = generics.get_object_or_404(Course, id=pk)
        subscription, created = Subscription.objects.get_or_create(
            user=request.user, course=course
        )
        if created:
            return Response(
                {"message": "Вы успешно подписались на обновления курса."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "Вы уже подписаны на обновления этого курса."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UnsubscribeApiView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        subscription = get_object_or_404(Subscription, user=request.user, course=course)

        subscription.delete()

        return Response(
            {"message": "Вы успешно отписались от обновлений курса."},
            status=status.HTTP_204_NO_CONTENT,
        )
