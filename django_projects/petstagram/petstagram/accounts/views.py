from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import UserCreateForm, LoginUserForm, UserEditForm

UserModel = get_user_model()


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home page')
    form_class = LoginUserForm


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home page')

    # After register user, doesn't need to log in to access the site!
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SingOutView(LogoutView):
    next_page = reverse_lazy('login user')


class DetailsUserView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('photolike_set')
        context['photo_count'] = photos.count()
        context['total_likes'] = sum(photo.photolike_set.count() for photo in photos)

        return context


class EditUserView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('username', 'first_name', 'last_name', 'image', 'gender',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.object.pk
        })


class DeleteUserView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('home page')
