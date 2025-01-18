from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from courses.models import Course, Lesson

User = get_user_model()


class CourseCRUDTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        self.client = APIClient()
        # self.client.login(email='testuser@example.com', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Test Course',
            description='Test Description',
            owner=self.user
        )

    def test_course_create(self):
        """Тест создания нового курса"""
        data = {
            'title': 'New Course',
            'description': 'New Description',
        }
        response = self.client.post('/api/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Course')
        self.assertEqual(response.data['description'], 'New Description')

    def test_course_read_list(self):
        """Тест получения списка курсов"""
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 4)
        # self.assertEqual(response.data[0]['title'], self.course.title)

    def test_course_read_detail(self):
        """Тест получения деталей конкретного курса"""
        response = self.client.get(f'/api/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['title'], self.course.title)
        self.assertEqual(response.data['description'], self.course.description)

    def test_course_update(self):
        """Тест обновления существующего курса"""
        data = {
            'title': 'Updated Course',
            'description': 'Updated Description',
        }
        response = self.client.put(f'/api/courses/{self.course.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Course')
        self.assertEqual(response.data['description'], 'Updated Description')

    def test_course_partial_update(self):
        """Тест частичного обновления курса (PATCH)"""
        data = {
            'title': 'Partially Updated Course',
        }
        response = self.client.patch(f'/api/courses/{self.course.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Partially Updated Course')
        self.assertEqual(response.data['description'], self.course.description)

    def test_course_delete(self):
        """Тест удаления курса"""
        response = self.client.delete(f'/api/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Course.objects.filter(id=self.course.id).exists())


class LessonCRUDTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='testpassword')
        self.client.login(email='testuser@example.com', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Test Course',
            description='Test Description',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='Test Lesson',
            description='Test Lesson Description',
            course=self.course,
            owner=self.user,
            video_url="http://youtube.com"
        )

    def test_lesson_create(self):
        data = {
            'title': 'New Lesson',
            'description': 'Lesson Description',
            'course': self.course.id,
            'video_url': "http://youtube.com",
        }
        response = self.client.post('/api/lessons/', data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Lesson')

    def test_lesson_read(self):
        response = self.client.get('/api/lessons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

        response = self.client.get(f'/api/lessons/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.lesson.title)

    def test_lesson_update(self):
        data = {
            'title': 'Updated Lesson',
            'description': 'Updated Lesson Description',
            'course': self.course.id,
            'video_url': "http://youtube.com",
        }
        response = self.client.put(f'/api/lessons/{self.lesson.id}/', data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Lesson')

    def test_lesson_delete(self):
        response = self.client.delete(f'/api/lessons/{self.lesson.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())
