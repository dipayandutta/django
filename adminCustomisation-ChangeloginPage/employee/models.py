from django.db import models

# Create your models here.
class EmpolyeeRecord(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    employee_salary = models.PositiveIntegerField()

    def __str__(self):
        return str(self.employee_id)
    
    class Meta:
        verbose_name = 'Employee Record'
        verbose_name_plural = 'Employees Record'

class EmployeePreviousExperience(models.Model):
    employee_id = models.ForeignKey(EmpolyeeRecord,on_delete=models.CASCADE)
    previous_company_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date   = models.DateTimeField()

    def __str__(self):
        return str(self.previous_company_name)
    
    class Meta:
        verbose_name = 'Employee Previous Experience'
        verbose_name_plural = 'Employee Previous Experiences'