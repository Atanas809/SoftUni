from django.urls import reverse_lazy

from fitness_world import settings
from fitness_world.common.models import LikePhoto
from tests.base.base_test_case import BaseTestCase


class LikePhotoTests(BaseTestCase):
    def test_like_photo__when_no_authenticated_user__expect_to_redirect(self):
        response = self.client.get(reverse_lazy('like photo', kwargs={'pk': 1}))

        expected_result = f"{settings.LOGIN_URL}?next={reverse_lazy('like photo', kwargs={'pk': 1})}"
        self.assertEqual(expected_result, response.headers['Location'])
        self.assertEqual(302, response.status_code)

    def test_like_photo__when_authenticated_user_like_new_photo__expect_create_like(self):
        user = self.create_and_login_user()

        photo = self.create_photos(user, count=1)[0]

        self.client.get(reverse_lazy('like photo', kwargs={'pk': photo.pk}), {}, HTTP_REFERER='http://127.0.0.1')

        likes = LikePhoto.objects.all()

        self.assertEqual(1, len(likes))

    def test_like_photo__when_authenticated_user_like_same_photo__expect_to_delete_like(self):
        user = self.create_and_login_user()

        photo = self.create_photos(user, count=1)[0]

        self.client.get(reverse_lazy('like photo', kwargs={'pk': photo.pk}), {}, HTTP_REFERER='http://127.0.0.1')
        self.client.get(reverse_lazy('like photo', kwargs={'pk': photo.pk}), {}, HTTP_REFERER='http://127.0.0.1')

        likes = LikePhoto.objects.all()

        self.assertEqual(0, len(likes))
