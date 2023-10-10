from django.test import TestCase

from lost_and_found.objects_posts.models import Object, Post


class BaseTestCase(TestCase):
    def create_post_with_object(self):
        create_object = Object(
            name='vase',
            image='https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639163872l/58293924.jpg',
            width=33,
            height=22,
            weight=50,
        )

        create_object.full_clean()
        create_object.save()

        create_post = Post(
            title='Adidas',
            description='Please help',
            author_name='Gogo',
            author_phone='0987654321',
            object_id=create_object.pk,
        )

        create_post.full_clean()
        create_post.save()

        return create_post

    def assertCollectionIsEmpty(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)
