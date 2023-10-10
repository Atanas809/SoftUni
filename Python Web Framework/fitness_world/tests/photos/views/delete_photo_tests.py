from django.urls import reverse_lazy

from fitness_world.photos.models import Photo
from tests import BaseTestCase


class DeletePhotoTests(BaseTestCase):
    def test_delete_photo__when_delete__expect_empty_collection(self):
        user = self.create_and_login_user()

        photo = self.create_photos(user, count=1)[0]

        self.client.post(reverse_lazy('delete photo', kwargs={'pk': photo.pk}))

        photos = Photo.objects.all()

        self.assertCollectionIsEmpty(photos)

    def test_delete_photo__when_2_photos__expect_only_1_left(self):
        user = self.create_and_login_user()

        photo = self.create_photos(user, count=2)[0]

        self.client.post(reverse_lazy('delete photo', kwargs={'pk': photo.pk}))

        photos = Photo.objects.all()

        self.assertEqual(1, len(photos))
