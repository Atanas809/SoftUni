from django.core.exceptions import ValidationError
from django.test import TestCase

from unit_integration_testing.web.models import Profile


class ProfileModelTests(TestCase):
    def test_profile_save__when_egn_is_valid__expect_correct_result(self):
        # Arrange

        profile = Profile(
            name='Gogo',
            age=22,
            egn='0233391119'
        )

        # Act

        profile.full_clean()  # Call this for validations
        profile.save()

        # Assert

        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_egn_have_less_than_10digits__expect_to_raise(self):
        # Arrange

        profile = Profile(
            name='Gogo',
            age=22,
            egn='929201234'
        )

        # Act

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        # Assert

        self.assertIsNotNone(ex.exception)

    def test_profile_save__when_egn_have_more_than_10digits__expect_to_raise(self):
        # Arrange

        profile = Profile(
            name='Gogo',
            age=22,
            egn='320402340909832',
        )

        # Act

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        # Assert

        self.assertIsNotNone(ex.exception)

    def test_profile_save__when_egn_have_letter__expect_to_raise(self):
        # Arrange

        profile = Profile(
            name='Gogo',
            age=22,
            egn='29103d2843',
        )

        # Act

        with self.assertRaises(ValidationError) as ex:
            profile.full_clean()
            profile.save()

        # Assert

        self.assertIsNotNone(ex.exception)
