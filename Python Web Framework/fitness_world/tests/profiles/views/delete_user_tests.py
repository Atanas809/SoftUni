from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from fitness_world.common.models import LikePhoto, CommentPhoto
from fitness_world.photos.models import Photo
from tests import BaseTestCase

UserModel = get_user_model()


class DeleteUserTests(BaseTestCase):
    def test_delete_user__when_deleting_user_data__expect_all_of_his_content_to_be_deleted(self):
        user = self.create_and_login_user()

        photos = self.create_photos(user, count=3)
        self.create_workouts(user, count=2)
        LikePhoto.objects.create(
            photo=photos[0],
            user=user,
        )
        CommentPhoto.objects.create(
            text='fdvfdvd',
            photo=photos[0],
            user=user,
        )

        self.client.post(reverse_lazy('delete user', kwargs={'pk': user.pk}))

        self.assertCollectionIsEmpty(UserModel.objects.all())
        self.assertCollectionIsEmpty(Photo.objects.all())
        self.assertCollectionIsEmpty(CommentPhoto.objects.all())
        self.assertCollectionIsEmpty(LikePhoto.objects.all())

