from django.contrib import admin

from fitness_world.common.models import LikePhoto, CommentPhoto


@admin.register(LikePhoto)
class LikePhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'user',)
    list_per_page = 5


@admin.register(CommentPhoto)
class CommentPhotoAdmin(admin.ModelAdmin):
    list_display = ('text', 'publication_date',)
    search_fields = ("text__icontains",)
    list_per_page = 5
