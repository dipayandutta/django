from django.db import models
from django.utils import timezone
# Create your models here.
class LogBook(models.Model):
    SerialNumber = models.AutoField(primary_key=True)
    CreatedAt    = models.DateField(default=timezone.now)
    Author       = models.TextField(max_length=30)
    Designation  = models.TextField(max_length=30)
    Subject      = models.TextField(max_length=300)
