from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import SimpleRouter

from config import settings
from lerning.apps import LerningConfig
from lerning.views import (CourseViewSet, LessonCreateApiView,
                           LessonDestroyAPIView, LessonListAPIView,
                           LessonRetrieveAPIView, LessonUpdateApiView,
                           SubscriptionApiView, UnsubscribeApiView)


app_name = LerningConfig.name

router = SimpleRouter()

router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path(
        "lesson/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"
    ),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path(
        "courses/<int:pk>/subscribe/", SubscriptionApiView.as_view(), name="subscribe"
    ),
    path(
        "courses/<int:pk>/unsubscribe", UnsubscribeApiView.as_view(), name="unsubscribe"
    ),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
