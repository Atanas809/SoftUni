from django import forms

from petstagram.common.models import PhotoLike, PhotoComment
from petstagram.photos.models import Photo
from petstagram.utils.disable_fields_mixin import DisableFieldsMixin


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'user',)

        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }


class PhotoDeleteForm(DisableFieldsMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = Photo
        exclude = ('photo', )

        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.pk).delete()
            PhotoComment.objects.filter(photo_id=self.instance.pk).delete()
            self.instance.delete()

        return self.instance


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('photo', )

        labels = {
            'photo': 'Photo file',
            'tagged_pets': 'Tag Pets',
        }
