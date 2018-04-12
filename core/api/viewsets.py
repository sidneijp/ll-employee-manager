from rest_framework import viewsets

from core.api.serializers import EmployeeReadSerializer, EmployeeSerializer
from core.api.utils import use_serializer
from core.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @use_serializer(EmployeeReadSerializer)
    def list(self, request):
        return super().list(request)

    @use_serializer(EmployeeReadSerializer)
    def retrieve(self, request, pk):
        return super().retrieve(request, pk)
