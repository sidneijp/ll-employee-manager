import django_filters

from core.models import Employee


class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(name="department__name")

    class Meta:
        model = Employee
        fields = ('name', 'department')
