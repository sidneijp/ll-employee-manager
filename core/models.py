from django.db import models
from django.utils.translation import ugettext_lazy as _


class Department(models.Model):
    name = models.CharField(_('Name'), max_length=160)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(_('Name'), max_length=160)
    email = models.EmailField(_('E-mail'), unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name=_('Department')
    )

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return self.name
