from django.urls import reverse

from lost_and_found.objects_posts.models import Post
from tests.base.base_test_case import BaseTestCase


class DeleteViewTests(BaseTestCase):
    def test_delete_view__when_delete_post__expect_post_to_be_deleted(self):
        post = self.create_post_with_object()
        post_pk = post.pk

        response = self.client.get(reverse('delete', kwargs={'pk': post_pk}))

        posts = Post.objects.filter(pk=post_pk)

        self.assertCollectionIsEmpty(posts)
        self.assertEqual(302, response.status_code)
