from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.base_test_case import BaseTestCase
from unit_integration_testing.web.models import Profile

UserModel = get_user_model()


class ProfileListViewTests(BaseTestCase):
    def test_profile_list_view__when_no_profiles__expect_to_return_empty_list_and_profiles_count(self):
        # self.client.get() --> makes HTTP GET request
        response = self.client.get(reverse('show profiles'))

        self.assertCollectionEmpty(response.context['profile_list'])
        self.assertEqual(0, response.context['profiles_count'])

    def test_profile_list_view__when_profiles__expect_to_return_list_and_profiles_count(self):
        profiles_count = 9
        profiles = [
            Profile(
                name=f'Gogo {i}',
                age=14 + i,
                egn=f'322333329{i}',
            )
            for i in range(1, profiles_count + 1)
        ]

        Profile.objects.bulk_create(profiles)
        response = self.client.get(reverse('show profiles'))

        self.assertListEqual(profiles, list(response.context['profile_list']))
        self.assertEqual(profiles_count, response.context['profiles_count'])

    def test_profile_list_view__when_anonymous_user__expect_to_return_username_anonymous(self):
        response = self.client.get(reverse('show profiles'))

        self.assertEqual('Anonymous', response.context['username'])

    def test_profile_list_view__when_logged_user__expect_to_return_username_correctly(self):
        username = 'Gogo'

        credentials = {
            'username': username,
            'password': 'qwert!23',
        }

        UserModel.objects.create_user(**credentials)

        self.client.login(**credentials)

        response = self.client.get(reverse('show profiles'))

        self.assertEqual(username, response.context['username'])

    def test_profile_list_view__when_no_query_params__expect_to_return_None(self):
        response = self.client.get(reverse('show profiles'))

        self.assertIsNone(response.context['query'])

    def test_profile_list_view__when_query_params__expect_to_return_correct_query(self):

        query_param = 'doncho2'

        response = self.client.get(
            reverse('show profiles'),
            data={
                'query': query_param,
            }
        )

        self.assertEqual(query_param, response.context['query'])

