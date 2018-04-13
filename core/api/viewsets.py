from rest_framework import viewsets

from core.api.serializers import EmployeeSerializer
from core.api.filters import EmployeeFilter
from core.api.utils import use_serializer
from core.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_class = EmployeeFilter
    lookup_field = 'email'
    lookup_value_regex = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
