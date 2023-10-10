from django.urls import reverse_lazy
from tests.base.base_test_case import BaseTestCase


class IndexTests(BaseTestCase):

    def test_index__when_no_authenticated_user__expect_is_authenticated_False(self):
        response = self.client.get(reverse_lazy('index'))

        user = response.context['user']

        self.assertFalse(user.is_authenticated)

    def test_index__when_authenticated_user__expect_is_authenticated_True(self):
        self.create_and_login_user()

        response = self.client.get(reverse_lazy('index'))

        self.assertTrue(response.context['user'].is_authenticated)

    def test_index__when_authenticated_user_and_no_photos__expect_empty_set(self):
        self.create_and_login_user()

        response = self.client.get(reverse_lazy('index'))

        photos = response.context['photos']

        self.assertCollectionIsEmpty(photos)

    def test_index__when_authenticated_user_and_photos__expect_correct_photos_count(self):
        user = self.create_and_login_user()
        photos = self.create_photos(user)

        self.client.get(reverse_lazy('index'))

        self.assertEqual(6, len(photos))

