from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from fitness_world.photos.models import Photo
from fitness_world.workouts.models import Workout

UserModel = get_user_model()


class BaseTestCase(TestCase):
    CREDENTIALS = {
        'username': 'gogo110',
        'email': 'gogo110@abv.bg',
        'password': 'Toni@34',
    }

    def create_comment(self):
        user = self.create_and_login_user()

        photo = self.create_photos(user, count=1)[0]

        self.client.post(
            reverse_lazy('comment photo', kwargs={'pk': photo.pk}),
            data={'text': 'Omg very cool'},
            HTTP_REFERER='http://127.0.0.1'
        )

        return user, photo

    def create_and_login_user(self, credentials=None):
        if credentials is None:
            credentials = self.CREDENTIALS

        user = UserModel.objects.create_user(**credentials)

        self.client.login(**credentials)

        return user

    @staticmethod
    def create_photos(user, count=6):
        photos = []

        for x in range(1, count + 1):
            photo = Photo.objects.create(
                image=f'images/axolotl{x}_GmxzBbK.jpeg',
                user=user,
            )

            photo.full_clean()
            photo.save()
            photos.append(photo)

        return photos

    def create_workouts(self, user, count=6):
        workouts = []

        for z in range(1, count + 1):
            workout = Workout(
                name=f'squads {z + 100}',
                reps=4,
                sets=9,
                link_to_image=f'https://upload.wikimedia.org/wikipedia/c{z}',
                user=user
            )

            workout.full_clean()
            workout.save()
            workouts.append(workout)

        return workouts

    def assertCollectionIsEmpty(self, collection):
        return self.assertEqual(0, len(collection), 'Collection is not empty!')

    def assertCollectionIsNotEmpty(self, collection):
        return self.assertNotEqual(0, len(collection), 'Collection is empty!')
