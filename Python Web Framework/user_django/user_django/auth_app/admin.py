from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from user_django.auth_app.forms import AppUserCreateForm

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    ordering = ('email',)
    list_filter = ()
    list_display = ('email', 'last_login',)
    add_form = AppUserCreateForm

    add_fieldsets = (
        (
            "Information",
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "age"),
            },
        ),
    )