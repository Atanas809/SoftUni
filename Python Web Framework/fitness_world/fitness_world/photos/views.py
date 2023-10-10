from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from fitness_world import settings
from fitness_world.common.forms import CommentCreateForm
from fitness_world.common.views import page_not_found
from fitness_world.core.core_utils import user_permissions
from fitness_world.core.photo_utils import photo_likes_count, photo_is_liked_by_user
from fitness_world.photos.forms import CreatePhotoForm, EditPhotoForm, DeletePhotoForm
from fitness_world.photos.models import Photo

UserModel = get_user_model()


class CreatePhotoView(LoginRequiredMixin, generic.CreateView):
    form_class = CreatePhotoForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        result = super().get_form_kwargs()
        result['user'] = self.request.user

        return result

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        photo.save()
        form.save_m2m()

        return super().form_valid(form)


class DetailsPhotoView(LoginRequiredMixin, generic.DetailView):
    template_name = 'photos/photo-details-page.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        photo_likes_count(self.object)
        photo_is_liked_by_user(self.request, self.object)

        context['is_owner'] = self.request.user == self.object.user
        context['comment_form'] = CommentCreateForm()

        return context


class EditPhotoView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = 'photos/photo-edit-page.html'
    form_class = EditPhotoForm
    model = Photo

    def test_func(self):
        try:
            photo = Photo.objects.get(pk=self.kwargs.get('pk'))
            user_pk = photo.user.pk
            owner = UserModel.objects.filter(pk=user_pk).get()
            return user_permissions(self.request, owner)
        except Photo.DoesNotExist:
            page_not_found(self.request)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        return page_not_found(self.request)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user

        return kwargs

    def get_success_url(self):
        return reverse_lazy('details photo', kwargs={
            'pk': self.object.pk
        })


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()

    if not user_permissions(request, photo.user):
        return page_not_found(request)

    if request.method == 'GET':
        form = DeletePhotoForm(instance=photo)
    else:
        form = DeletePhotoForm(request.POST, instance=photo)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, 'photos/photo-delete-page.html', context)
