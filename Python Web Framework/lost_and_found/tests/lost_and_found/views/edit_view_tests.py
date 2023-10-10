from django.urls import reverse

from lost_and_found.objects_posts.models import Post
from tests.base.base_test_case import BaseTestCase


class EditViewTests(BaseTestCase):
    def test_edit_view__when_get_method__expect_data_to_be_the_same(self):
        post = self.create_post_with_object()
        title_before_edit = post.title

        response = self.client.get(reverse('edit', kwargs={'pk': post.pk}))

        post = Post.objects.filter(pk=post.pk).get()

        title_after_edit = post.title

        self.assertEqual(title_before_edit, title_after_edit)

    def test_edit_view__when_post_method_and_change_title__expect_title_to_be_changed(self):
        post = self.create_post_with_object()
        title_before_edit = post.title

        data_with_changed_title = {
            'title': 'Nike',
            'description': 'Please help',
            'author_name': 'Gogo',
            'author_phone': '0987654321',
        }

        response = self.client.post(reverse('edit', kwargs={'pk': post.pk}), data=data_with_changed_title)

        post = Post.objects.filter(pk=post.pk).get()

        title_after_edit = post.title

        self.assertNotEqual(title_before_edit, title_after_edit)

    def test_edit_view__when_post_method_and_doest_change_anything__expect_title_to_be_the_same(self):
        post = self.create_post_with_object()
        title_before_edit = post.title

        response = self.client.post(reverse('edit', kwargs={'pk': post.pk}))

        post = Post.objects.filter(pk=post.pk).get()

        title_after_edit = post.title

        self.assertEqual(title_before_edit, title_after_edit)
