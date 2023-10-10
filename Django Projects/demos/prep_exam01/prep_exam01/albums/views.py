from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from prep_exam01.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from prep_exam01.albums.models import Album
from django.views import generic


# Create your views here.


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'albums/add-album.html', context)


class EditAlbum(generic.UpdateView):
    model = Album
    fields = '__all__'
    template_name = 'albums/edit-album.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'id'
    context_object_name = 'album'


def details_album(request, id):
    album = Album.objects.filter(pk=id).get()

    context = {
        'album': album,
    }

    return render(request, 'albums/album-details.html', context)


class DeleteAlbum(generic.DeleteView):
    template_name = 'albums/delete-album.html'
    form_class = AlbumDeleteForm
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_queryset().get()
        context = self.get_context_data(album=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=context['object'])
        return context

    def get_queryset(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Album.objects.filter(pk=pk)

