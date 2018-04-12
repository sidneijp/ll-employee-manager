import pytest

from core.models import Employee
from . import factories


@pytest.mark.django_db
def test_create_employee(client, department):
    employee = factories.EmployeeFactory.build(department=department)
    data = {
        'name': employee.name,
        'email': employee.email,
        'department': employee.department.pk,
    }
    response = client.post('/employee/', data)
    assert response.status_code == 201
    last_inserted_employee = Employee.objects.last()
    assert last_inserted_employee.email == employee.email
