from django.contrib import admin

from unit_integration_testing.web.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
