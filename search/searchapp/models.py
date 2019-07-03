from django.db import models
from django.utils import timezone
# Create your models here.
class Student(models.Model):
    name    = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50)
    city    = models.CharField(max_length=50,blank=True,null=True)
    marks   = models.IntegerField(default=0,blank=True,null=True)
    date    = models.DateTimeField(auto_now=True)