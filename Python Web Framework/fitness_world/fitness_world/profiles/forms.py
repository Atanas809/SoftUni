from django.contrib.auth import forms as auth_forms, get_user_model, password_validation
from django import forms
from django.contrib.auth.forms import UsernameField


UserModel = get_user_model()


class SignInForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                'placeholder': 'Username'
            }
        )
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'placeholder': 'Password',
            }
        ),
    )


class UserCreateForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Repeat Password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = UserModel
        fields = ("username", 'email', 'password1', 'password2',)
        field_classes = {"username": auth_forms.UsernameField}

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            )
        }


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"
        field_classes = {"username": UsernameField}
