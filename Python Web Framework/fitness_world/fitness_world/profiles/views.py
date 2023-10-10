from django.contrib.auth import views as auth_views, get_user_model, login
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy

from fitness_world import settings
from fitness_world.common.views import page_not_found
from fitness_world.core.core_utils import user_permissions
from fitness_world.core.photo_utils import photo_likes_count
from fitness_world.core.user_utils import likes_for_photos_delete, comments_for_photos_delete, workouts_delete
from fitness_world.photos.models import Photo
from fitness_world.profiles.forms import SignInForm, UserCreateForm
from fitness_world.workouts.models import Workout

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    form_class = SignInForm
    template_name = 'profiles/login-page.html'


class SignUpView(generic.CreateView):
    template_name = 'profiles/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    # After register user, doesn't need to log in to access the site!
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignOutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('index')


class DeleteUserView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, generic.DeleteView):
    template_name = 'profiles/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def test_func(self):
        try:
            user_pk = self.kwargs.get('pk')
            owner = UserModel.objects.filter(pk=user_pk).get()
            return user_permissions(self.request, owner)
        except UserModel.DoesNotExist:
            page_not_found(self.request)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        return page_not_found(self.request)

    def form_valid(self, form):
        success_url = self.get_success_url()

        owned_photos = Photo.objects.filter(user_id=self.object.pk).all()

        workouts_delete(user=self.object)
        likes_for_photos_delete(owned_photos, self.object)
        comments_for_photos_delete(owned_photos, self.object)
        owned_photos.delete()

        self.object.delete()
        return redirect(success_url)


class DetailsUserView(auth_mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'profiles/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        owned_photos = Photo.objects.filter(user_id=self.object.pk).all()

        context['is_owner'] = self.request.user == self.object
        context['have_full_name'] = self.object.first_name and self.object.last_name
        context['total_photos_owned'] = owned_photos
        context['total_workouts_owned'] = Workout.objects.filter(user_id=self.object.pk).count()
        context['ordered_photos'] = owned_photos.order_by('-date_of_publication')

        owned_photos = [photo_likes_count(photo) for photo in owned_photos]
        context['total_likes'] = sum(p.likes for p in owned_photos)

        return context


class EditUserView(auth_mixins.LoginRequiredMixin, auth_mixins.UserPassesTestMixin, generic.UpdateView):
    template_name = 'profiles/profile-edit-page.html'
    model = UserModel
    fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'weight', 'gender')

    def test_func(self):
        try:
            user_pk = self.kwargs.get('pk')
            owner = UserModel.objects.filter(pk=user_pk).get()
            return user_permissions(self.request, owner)
        except UserModel.DoesNotExist:
            page_not_found(self.request)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        return page_not_found(self.request)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.object.pk,
        })

