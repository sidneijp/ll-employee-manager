from rest_framework import viewsets

from core.api.serializers import EmployeeSerializer
from core.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
