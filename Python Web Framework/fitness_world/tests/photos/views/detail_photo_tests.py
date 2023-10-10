from django.urls import reverse_lazy

from tests import BaseTestCase


class DetailPhotoTests(BaseTestCase):
    def test_detail_photo__when_user_is_not_owner_of_the_photo__expect_is_owner_to_be_false(self):
        user1 = self.create_and_login_user()
        photo = self.create_photos(user1, count=1)[0]
        self.client.logout()

        user2 = self.create_and_login_user({
            'username': 'gogo11011',
            'email': 'goggo110@abv.bg',
            'password': 'Toooni@34',
        })

        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photo.pk}))

        is_owner = response.context['is_owner']

        self.assertFalse(is_owner)

    def test_detail_photo__when_user_is_owner_of_the_photo__expect_is_owner_to_be_true(self):
        user1 = self.create_and_login_user()
        photo = self.create_photos(user1, count=1)[0]

        response = self.client.get(reverse_lazy('details photo', kwargs={'pk': photo.pk}))

        is_owner = response.context['is_owner']

        self.assertTrue(is_owner)
