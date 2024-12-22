from rest_framework import serializers

from lerning.models import Course, Lesson, Subscription
from lerning.validators import LinksValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        # validators = [LinksValidator(field=['name', 'description'])]
        extra_kwargs = {
            "video_link": {"validators": [LinksValidator(field="video_link")]},
            "description": {"validators": [LinksValidator(field="description")]},
        }


class CourseSerializer(serializers.ModelSerializer):
    quantity_lesson = serializers.SerializerMethodField()
    info_lesson = serializers.SerializerMethodField()

    def get_quantity_lesson(self, odj):
        return odj.lessons.count()

    def get_info_lesson(self, obj):
        return LessonSerializer(obj.lessons.all(), many=True).data

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "description",
            "quantity_lesson",
            "info_lesson",
            "owner",
        )

        validators = [LinksValidator(field=["name", "description"])]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
