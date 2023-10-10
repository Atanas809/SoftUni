from unittest import TestCase

from django.core.exceptions import ValidationError

from unit_integration_testing.web.validators import egn_validator


class EgnValidatorTests(TestCase):
    def test_egn_validator__when_valid__expect_ok(self):
        value = egn_validator('1234567890')

        self.assertIsNone(value)

    def test_egn_validator__when_less_than_10digits__expect_to_raise(self):
        with self.assertRaises(ValidationError) as ex:
            egn_validator('123456790')

        self.assertIsNotNone(ex.exception)

    def test_egn_validator__when_more_than_10digits__expect_to_raise(self):
        with self.assertRaises(ValidationError) as ex:
            egn_validator('12345679550')

        self.assertIsNotNone(ex.exception)

    def test_egn_validator__when_non_digit__expect_to_raise(self):
        with self.assertRaises(ValidationError) as ex:
            egn_validator('123456n790')

        self.assertIsNotNone(ex.exception)
