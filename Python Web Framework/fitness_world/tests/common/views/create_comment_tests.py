from django.urls import reverse_lazy

from fitness_world.common.models import CommentPhoto
from tests.base.base_test_case import BaseTestCase


class CreateCommentTests(BaseTestCase):
    def test_create_comment__when_comment_specific_photo__expect_comment_to_be_added(self):
        user, photo = self.create_comment()

        comments = CommentPhoto.objects.all()

        self.assertEqual(1, len(comments))
        self.assertEqual(user, comments[0].user)
        self.assertEqual(photo, comments[0].photo)
