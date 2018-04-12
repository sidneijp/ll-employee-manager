import pytest

from .factories import DepartmentFactory


@pytest.fixture
def department():
    return DepartmentFactory.create()
