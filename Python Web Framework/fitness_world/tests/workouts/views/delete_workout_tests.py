from django.urls import reverse_lazy

from fitness_world.workouts.models import Workout
from tests import BaseTestCase


class DeleteWorkoutTests(BaseTestCase):
    def test_delete_workout__when_delete__expect_given_workout_to_be_deleted(self):
        user = self.create_and_login_user()

        workout = self.create_workouts(user, count=1)[0]

        self.client.post(reverse_lazy('delete workout', kwargs={'username': user.username, 'slug': workout.slug}))

        self.assertCollectionIsEmpty(Workout.objects.all())

    def test_delete_workout__when_2_workouts__expect_only_1_left(self):
        user = self.create_and_login_user()

        workout = self.create_workouts(user, count=2)[0]

        self.client.post(reverse_lazy('delete workout', kwargs={'username': user.username, 'slug': workout.slug}))

        self.assertEqual(1, len(Workout.objects.all()))
