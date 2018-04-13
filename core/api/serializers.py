from rest_framework import serializers

from core.models import Department, Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Department.objects.all(),
    )

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')
