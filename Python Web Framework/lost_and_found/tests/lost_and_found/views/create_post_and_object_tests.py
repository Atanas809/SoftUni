from django.urls import reverse

from lost_and_found.objects_posts.models import Object, Post
from tests.base.base_test_case import BaseTestCase


class CreatePostObjectTests(BaseTestCase):
    def test_create_view__when_get_method__expect_same_page(self):
        response = self.client.get(reverse('create'))

        objects = Object.objects.all()
        posts = Post.objects.all()

        self.assertCollectionIsEmpty(objects)
        self.assertCollectionIsEmpty(posts)
        self.assertEqual(200, response.status_code)

    def test_create_view__when_post_method__expect_object_and_post_to_be_created(self):
        object_and_post_data = {
            'name': 'vase',
            'image': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639163872l/58293924.jpg',
            'width': 33,
            'height': 22,
            'weight': 50,
            'title': 'Adidas',
            'description': 'Please help',
            'author_name': 'Gogo',
            'author_phone': '0987654321',
        }

        response = self.client.post(reverse('create'), data=object_and_post_data)

        objects = Object.objects.all()
        posts = Post.objects.all()

        self.assertEqual(1, len(objects))
        self.assertEqual(1, len(posts))
        self.assertEqual(302, response.status_code)
        self.assertEqual('/', response.headers['Location'])

    def test_create_view__when_post_method_and_invalid_data_passed__expect_empty_query_set(self):
        object_and_post_data = {
            'name': 'vase',
            'image': 'https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639163872l/58293924.jpg',
            'width': 33,
            'height': 22,
            'weight': 50,
            'title': 'Adidas',
            'description': 'Please help',
            'author_name': 'Gogo',
            'author_phone': '098765432142',
        }

        response = self.client.post(reverse('create'), data=object_and_post_data)

        objects = Object.objects.all()
        posts = Post.objects.all()

        self.assertEqual(0, len(objects))
        self.assertEqual(0, len(posts))
        self.assertEqual(200, response.status_code)
