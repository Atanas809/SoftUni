from django.contrib import admin

from exercises_for_web.common.models import PhotoComment, PhotoLike


# Register your models here.

@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    ordering = ('-publication_date_and_time', )


@admin.register(PhotoLike)
class PhotoLikeAdmin(admin.ModelAdmin):
    pass
