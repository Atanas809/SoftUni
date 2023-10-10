from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic as views

from user_django.auth_app.forms import SignUpForm
from user_django.auth_app.models import Profile

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users list')

    # After register user, doesn't need to log in to access the site!
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


# Login with function-base view
# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#
#             user = authenticate(request, username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 return redirect('users list')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-in.html', context)


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    # First way to redirect when valid credentials: (Use this instead of second way!!!!!!)
    next_page = reverse_lazy('users list')

    # Second way to redirect when valid credentials:
    # success_url = reverse_lazy('users list')
    #
    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #
    #     return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(LogoutView):
    template_name = 'auth/sign-out.html'


class DeleteProfile(views.DeleteView):
    model = UserModel
    success_url = reverse_lazy('users list')
    template_name = 'web/delete-user.html'
    #
    # def delete(self, request, *args, **kwargs):
    #     """
    #     Call the delete() method on the fetched object and then redirect to the
    #     success URL.
    #     """
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     # Profile.objects.filter(user=self.object.pk).delete()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)
