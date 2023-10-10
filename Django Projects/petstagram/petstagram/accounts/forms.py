from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm, UserChangeForm
from django import forms

UserModel = get_user_model()


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {"username": UsernameField}


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", 'email')
        field_classes = {"username": UsernameField}


class LoginUserForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'placeholder': 'Password'}),
    )
