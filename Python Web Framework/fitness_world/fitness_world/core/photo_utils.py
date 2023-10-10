from fitness_world.common.models import LikePhoto


def photo_likes_count(photo):
    photo.likes = photo.likephoto_set.count()
    return photo


def photo_is_liked_by_user(request, photo):
    liked = LikePhoto.objects.filter(photo_id=photo.pk, user_id=request.user.pk)

    photo.liked_by_user = True if liked else False

    return photo
