from django.urls import reverse

from lost_and_found.objects_posts.models import Post
from tests.base.base_test_case import BaseTestCase


class FoundViewTests(BaseTestCase):
    def test_found_view__when_get_method__expect_to_be_founded(self):
        post = self.create_post_with_object()
        before_found = post.found

        self.client.get(reverse('found', kwargs={'pk': post.pk}))

        post = Post.objects.filter(pk=post.pk).get()

        after_found = post.found

        self.assertNotEqual(before_found, after_found)




