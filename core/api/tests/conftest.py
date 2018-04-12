import pytest

from .factories import DepartmentFactory, EmployeeFactory


@pytest.fixture
def department():
    return DepartmentFactory.create()


@pytest.fixture
def employee(department):
    return EmployeeFactory.create(department=department)


@pytest.fixture
def employees(department):
    return EmployeeFactory.create_batch(2, department=department)
