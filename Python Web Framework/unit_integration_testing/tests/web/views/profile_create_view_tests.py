from django.conf import settings
from django.urls import reverse

from tests.base.base_test_case import BaseTestCase
from unit_integration_testing.web.models import Profile


class ProfileCreateViewTests(BaseTestCase):
    def test_profile_create_view__when_logged_user__expect_to_create_profile(self):
        profile_data = {
            'name': 'Gogo',
            'age': 22,
            'egn': '3910718213',
        }

        credentials = {
            'username': 'Gogo',
            'password': 'qwerty123'
        }

        self.create_and_log_in_user(**credentials)

        response = self.client.post(reverse('create profile'), data=profile_data)

        created_profile = Profile.objects.filter(**profile_data).get()

        self.assertIsNotNone(created_profile)
        self.assertEqual(302, response.status_code)

    def test_profile_create_view__when_anonymous_user__expect_to_raise(self):
        profile_data = {
            'name': 'Gogo',
            'age': 22,
            'egn': '3910718213',
        }

        response = self.client.post(reverse('create profile'), data=profile_data)

        created_profile = Profile.objects.filter(**profile_data)

        # First way:
        # self.assertCollectionEmpty(created_profile)
        # self.assertEqual(302, response.status_code)

        # Second way:
        expected_result = f"{settings.LOGIN_URL}?next={reverse('create profile')}"
        self.assertEqual(expected_result, response.headers.get('Location'))
        self.assertEqual(302, response.status_code)
