import factory

from core.models import Department, Employee


class DepartmentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Department


class EmployeeFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.Faker('email')
    department = factory.SubFactory(DepartmentFactory)

    class Meta:
        model = Employee

