from django.contrib import admin

from core.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'department',)
    search_fields = ('email', 'name',)
    list_filter = ('department',)


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
