import pytest

from core.models import Employee
from . import factories


@pytest.mark.django_db
def test_create_employee(authenticated_client, department):
    employee = factories.EmployeeFactory.build(department=department)
    data = {
        'name': employee.name,
        'email': employee.email,
        'department': employee.department.pk,
    }
    response = authenticated_client.post('/employee/', data)
    assert response.status_code == 201
    last_inserted_employee = Employee.objects.last()
    assert last_inserted_employee.email == employee.email


@pytest.mark.django_db
def test_list_employee(authenticated_client, employees):
    expected_amount = Employee.objects.all().count()
    response = authenticated_client.get('/employee/')
    assert response.status_code == 200
    amount = len(response.json())
    assert expected_amount == amount


@pytest.mark.django_db
def test_list_filter_employee(authenticated_client, departments, employees):
    department = departments.pop()
    expected_amount = Employee.objects.filter(department=department).count()
    data = {'department': department.pk}
    response = authenticated_client.get('/employee/', data)
    assert response.status_code == 200
    json_response = response.json()
    amount = len(json_response)
    assert expected_amount == amount
    assert department.name in [_.get('department') for _ in json_response]


@pytest.mark.django_db
def test_get_employee(authenticated_client, employee):
    response = authenticated_client.get('/employee/%s/' % employee.pk)
    assert response.status_code == 200
    json_response = response.json()
    assert employee.email == json_response.get('email')
    assert employee.department.name == json_response.get('department')
    expected_fields = ('name', 'email', 'department')
    fields = json_response.keys()
    for expected_field in expected_fields:
        assert expected_field in fields
    assert len(expected_fields) == len(fields)


@pytest.mark.django_db
def test_delete_employee(authenticated_client, employee):
    response = authenticated_client.delete('/employee/%s/' % employee.pk)
    assert response.status_code == 204
    invalid_id = -1
    response = authenticated_client.delete('/employee/%s/' % invalid_id)
    assert response.status_code == 404


@pytest.mark.django_db
def test_unauthorized_api_call(client, employees):
    response = client.get('/employee/')
    assert response.status_code == 403
