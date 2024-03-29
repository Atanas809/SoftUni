from rest_framework import serializers

from django_rest_demo.web.models import Employee, Department


class ShortEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'salary',)


class DepartmentSerializer(serializers.ModelSerializer):
    employee_set = ShortEmployeeSerializer(many=True)

    class Meta:
        model = Department
        fields = '__all__'


class ShortDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = ShortDepartmentSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        department_name = validated_data.pop('department').get('name')

        return Employee.objects.create(
            **validated_data,
            department=Department.objects.get_or_create_by_name(department_name),
        )


class NameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class DemoSerializer(serializers.Serializer):
    employees = ShortEmployeeSerializer(many=True)
    employees_count = serializers.IntegerField()
    departments = ShortDepartmentSerializer(many=True)
    first_department = serializers.CharField(max_length=50)
    departments_names = NameSerializer(many=True)
