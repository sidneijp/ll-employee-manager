from django.contrib import admin

from core.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
