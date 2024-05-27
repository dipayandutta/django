from django.contrib import admin
from .models import Students
# Register your models here.

#admin.site.register(Students)
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Informations',{
            'fields': ('firstName','lastName','age','gender','address')
        }),
        ('School Details',{
            'fields':('school_name','standard')
        }),
        ('Parent Details',{
            'fields':('father_name','mother_name','parent_contact_number'),
        }),
    )

