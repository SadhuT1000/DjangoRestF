# flake8: noqa


from django.urls import reverse
from rest_framework import status
from rest_framework.test import  APITestCase
from lerning.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="admin@example.com", is_staff=True, is_superuser=True, is_active=True
        )

        self.course = Course.objects.create(
            name="Python2", description="middle level", owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name="Python2",
            description="middle level",
            owner=self.user,
            course=self.course,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lerning:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)
        self.assertEqual(data.get("description"), self.course.description)

    def test_lesson_create(self):

        url = reverse(
            "lerning:lesson_create",
        )

        data = {
            "name": "JavaScript",
            "lesson": "ООП",
            "description": "Base_course",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lerning:lesson_update", args=(self.lesson.pk,))

        data = {"name": "Python4"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Python4")

    def test_lesson_delete(self):
        url = reverse("lerning:lesson_delete", args=(self.lesson.pk,))

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lerning:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": "Python2",
                    "description": "middle level",
                    "preview": None,
                    "link_video": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                },
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="admin@example.com",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            password="123qwe",
        )
        self.course = Course.objects.create(
            name="Python2", description="middle level", owner=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):

        url = reverse("lerning:subscribe", args=(self.course.pk,))

        data = {
            "user": self.user.pk,
            "course": self.course.pk,
        }

        response = self.client.post(url, data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_subscription_delete(self):

        url = reverse("lerning:unsubscribe", args=(self.course.pk,))
        data = {
            "course": self.course.pk,
        }
        Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.delete(url, data)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            response.data, {"message": "Вы успешно отписались от обновлений курса."}
        )
        self.assertEqual(Subscription.objects.count(), 0)


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="admin@example.com", is_staff=True, is_superuser=True, is_active=True
        )

        self.course = Course.objects.create(
            name="Python2", description="middle level", owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name="ООП", description="repeat", owner=self.user, course=self.course
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):

        url = reverse("lerning:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)
        self.assertEqual(data.get("description"), self.course.description)

    # def test_course_create(self):
    #     url = reverse("lerning:course-list",)
    #
    #     data = {
    #         "name": "JavaScript",
    #         "lesson": "ООП",
    #         "description": "Base_course",
    #
    #     }
    #     #response = self.client.post(url, data={'field_name': [{'url': 'https://youtube.com'}]})
    #
    #     response = self.client.post(url, data)
    #     print(response.json())
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Course.objects.all().count(), 1)
    # def test_course_update(self):
    #      url = reverse("lerning:course-detail", args=(self.course.pk,))
    #
    #     data = {
    #         "name": "Python1"
    #     }
    #     response = self.client.patch(url, data)
    #     data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data.get("name"), "Python1")

    def test_course_delete(self):
        url = reverse("lerning:course-detail", args=(self.course.pk,))

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_course_list(self):
        url = reverse("lerning:course-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
