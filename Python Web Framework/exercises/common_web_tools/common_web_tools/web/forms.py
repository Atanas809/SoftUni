from django import forms
from django.contrib.auth.models import User

from common_web_tools.web.models import Student, Profile


class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('student',)
