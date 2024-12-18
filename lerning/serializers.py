
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from lerning.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    quantity_lesson = serializers.SerializerMethodField()
    info_lesson = serializers.SerializerMethodField()

    def get_quantity_lesson(self, odj):
        return odj.lessons.count()

    def get_info_lesson(self, obj):
        return LessonSerializer(obj.lessons.all(), many=True).data
    class Meta:
        model = Course
        fields = ("id", "name", "description", "quantity_lesson", "info_lesson")





