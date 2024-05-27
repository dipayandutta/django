from django.db import models

# Create your models here.

GENDER = [
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
]

class Students(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=GENDER)
    address = models.CharField(max_length=200)
    school_name = models.CharField(max_length=100)
    standard = models.IntegerField()
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    parent_contact_number = models.CharField(max_length=10)


    class Meta:
        verbose_name = "Student Detail"
        verbose_name_plural = "Student Details"


    def __str__(self):
        return (f"{self.firstName}{self.lastName}")


