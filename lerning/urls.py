from django.urls import path
from rest_framework.routers import SimpleRouter
from django.conf.urls.static import static
from config import settings
from lerning.apps import LerningConfig
from lerning.views import (CourseViewSet, LessonCreateApiView,
                           LessonDestroyAPIView, LessonListAPIView,
                           LessonRetrieveAPIView, LessonUpdateApiView)
from users.views import PaymentsViewSet, UserViewSet

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
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
