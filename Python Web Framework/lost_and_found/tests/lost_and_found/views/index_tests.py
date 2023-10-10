from django.test import TestCase
from django.urls import reverse

from lost_and_found.objects_posts.models import Post, Object
from tests.base.base_test_case import BaseTestCase


class IndexTests(BaseTestCase):
    def test_index_view__when_no_posts__expect_empty_result(self):
        response = self.client.get(reverse('index'))

        self.assertCollectionIsEmpty(response.context['posts'])

    def test_index_view__when_posts__expect_correct_result(self):

        self.create_post_with_object()
        self.create_post_with_object()

        response = self.client.get(reverse('index'))

        posts = response.context['posts']

        self.assertEqual(2, len(posts))
