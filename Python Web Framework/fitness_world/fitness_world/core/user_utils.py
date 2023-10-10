from fitness_world.common.models import CommentPhoto, LikePhoto
from fitness_world.workouts.models import Workout


def workouts_delete(user):
    Workout.objects.filter(user_id=user.pk).all().delete()


def likes_for_photos_delete(photos, user):
    for photo in photos:
        photo.likephoto_set.all().delete()

    LikePhoto.objects.filter(user_id=user.pk).all().delete()


def comments_for_photos_delete(photos, user):
    photos_pks = [p.pk for p in photos]
    CommentPhoto.objects.filter(user_id=user.pk).all().delete()
    CommentPhoto.objects.filter(photo_id__in=photos_pks).all().delete()
