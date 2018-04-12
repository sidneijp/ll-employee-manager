import pytest

from .factories import DepartmentFactory, EmployeeFactory


@pytest.fixture
def department():
    return DepartmentFactory.create()


@pytest.fixture
def departments():
    return DepartmentFactory.create_batch(2)


@pytest.fixture
def employee(department):
    return EmployeeFactory.create(department=department)


@pytest.fixture
def employees(departments):
    department_1, department_2 = departments
    EmployeeFactory.create_batch(2, department=department_1)
    return EmployeeFactory.create_batch(2, department=department_2)
