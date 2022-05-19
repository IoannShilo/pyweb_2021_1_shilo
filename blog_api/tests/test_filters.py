from django.test import TestCase
from django.contrib.auth.models import User

from blog_api import filters
from blog.models import Note


class TestNoteFilter(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_1 = User(
            username="test_user",
            password="qwerty"
        )
        test_user_2 = User(
            username="test_user_2",
            password="qwerty"
        )

        test_user_1, test_user_2 = User.objects.bulk_create([test_user_1, test_user_2])

        Note.objects.create(
            title="title_1",
            public=False,
            author=test_user_1
        )
        Note.objects.create(
            title="title_2",
            public=True,
            author=test_user_2
        )

    def test_filter_notes_by_author_id(self):
        filter_author_id = 1
        queryset = Note.objects.all()

        expected_queryset = queryset.filter(author_id=filter_author_id)

        actual_queryset = filters.filter_notes_by_author_id(queryset, filter_author_id)

        self.assertQuerysetEqual(actual_queryset, expected_queryset)

        # queryset.filter(author__username=)
