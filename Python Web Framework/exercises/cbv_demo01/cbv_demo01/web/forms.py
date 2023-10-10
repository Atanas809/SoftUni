from django import forms

from cbv_demo01.web.models import Employee


class CreateEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
