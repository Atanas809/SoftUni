from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms

from user_django.auth_app.models import Profile

UserModel = get_user_model()


class AppUserCreateForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        # fields = ("first_name", "last_name", "username",)
        fields = (UserModel.USERNAME_FIELD, 'first_name', 'last_name', 'age')
        field_classes = {"username": UsernameField}

    # Creates User and add this user to EMPTY profile
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     profile = Profile(
    #         user=user,
    #     )
    #
    #     if commit:
    #         profile.save()
    #
    #     return user

    # Creates User and add this user to profile with user data
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            user=user,
        )

        if commit:
            profile.save()

        return user


class SignUpForm(AppUserCreateForm):
    pass


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
