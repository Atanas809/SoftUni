from django.contrib import admin

from petstagram.common.models import PhotoComment, PhotoLike


# Register your models here.

@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PhotoLike)
class PhotoLikeAdmin(admin.ModelAdmin):
    pass
