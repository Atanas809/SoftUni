from django.urls import reverse_lazy

from fitness_world.common.models import CommentPhoto
from tests.base.base_test_case import BaseTestCase


class DeleteCommentTests(BaseTestCase):
    def test_delete_comment__when_get_method__expect_one_comment(self):
        user, photo = self.create_comment()

        comment_before = CommentPhoto.objects.all()[0]

        self.client.get(reverse_lazy('delete comment', kwargs={'pk': comment_before.pk}))

        comment_after = CommentPhoto.objects.all()

        self.assertCollectionIsNotEmpty(comment_after)
        self.assertCollectionIsNotEmpty(photo.commentphoto_set.all())
        self.assertCollectionIsNotEmpty(user.commentphoto_set.all())

    def test_delete_comment__when_post_method__expect_empty_collection(self):
        user, photo = self.create_comment()

        comment_before = CommentPhoto.objects.all()[0]

        self.client.post(reverse_lazy('delete comment', kwargs={'pk': comment_before.pk}))

        comment_after = CommentPhoto.objects.all()

        self.assertCollectionIsEmpty(comment_after)
        self.assertCollectionIsEmpty(photo.commentphoto_set.all())
        self.assertCollectionIsEmpty(user.commentphoto_set.all())
