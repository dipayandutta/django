from django.contrib import admin
from .models import EmpolyeeRecord,EmployeePreviousExperience
# Register your models here.

# inline a model in another model to Django admin Panel.

class EmployeePrevioysExperiencdAdmin(admin.TabularInline):
    model = EmployeePreviousExperience
    extra = 1

@admin.register(EmpolyeeRecord)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('employee_name','designation','employee_salary')
    inlines = [EmployeePrevioysExperiencdAdmin,]

