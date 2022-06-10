import django.contrib.auth
from django.test import Client
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from blog.models import Note


class TestNotePublicListAPIView(APITestCase):

    def test_get_public_notes(self):
        test_user = User.objects.create(
            username="test_user",
            password="qwerty"
        )

        Note.objects.create(title="title_1", public=False, author=test_user)
        Note.objects.create(title="title_2", public=True, author=test_user)

        path = "/notes/"
        resp = self.client.get(path)
        self.assertEqual(
            resp.status_code, status.HTTP_200_OK
        )
        data = resp.data
        expected_count_public_notes = 1
        self.assertEqual(
            len(data), expected_count_public_notes
        )

        for note in data:
            self.assertTrue(note["public"])

    def test_post_note(self):
        user = User.objects.create(username="admin", password="admin")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        data = {'title': "title_2", 'public': True, 'deadline': '2022-06-09'}
        path = "/notes/"
        resp = self.client.post(path, data)
        print(resp.status_code)
        self.assertEqual(
            resp.status_code, status.HTTP_201_CREATED
        )

    def test_patch_note(self):
        # Создаем двух пользователей
        user = User.objects.create(username="user1", password="user1")
        user_2 = User.objects.create(username="user2", password="user2")
        # создаем запись от первого пользователя
        Note.objects.create(title="title_2", public=True, deadline='2022-06-09', author_id='1')

        note_pk = 1
        url = f"/notes/{note_pk}"
        # логинимся под первым пользователем и пытаемся изменить запись
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        resp = self.client.patch(url, data={'title': 'new_title'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # логинимся под вторым пользователем и пытаемся изменить запись
        self.client = APIClient()
        self.client.force_authenticate(user=user_2)
        resp_2 = self.client.patch(url, data={'title': 'new_title'})
        self.assertEqual(resp_2.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_note(self):
        # Создаем двух пользователей
        user = User.objects.create(username="admin", password="admin")
        user_2 = User.objects.create(username="user", password="user")
        # создаем запись от первого пользователя
        Note.objects.create(title="title_2", public=True, deadline='2022-06-09', author_id='1')

        note_pk = 1
        url = f"/notes/{note_pk}"

        # логинимся под первым пользователем и проверяем наличие записи
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # пытаемся удалить запись
        resp_2 = self.client.delete(url)
        self.assertEqual(resp_2.status_code, status.HTTP_204_NO_CONTENT)

        # логинимся под вторым пользователем и пытаемся удалить запись
        self.client = APIClient()
        self.client.force_authenticate(user=user_2)

        resp_2 = self.client.delete(url)
        self.assertEqual(resp_2.status_code, status.HTTP_403_FORBIDDEN)
