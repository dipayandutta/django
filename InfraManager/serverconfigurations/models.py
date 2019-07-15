from django.db import models
from django.utils import timezone
# Create your models here.
class ServerDetails(models.Model):
    SerialNumber    = models.AutoField(primary_key=True)
    CreatedAt       = models.DateField(default=timezone.now)
    ipaddress       = models.TextField(max_length=40)
    hdd             = models.TextField(max_length=10)
    ram             = models.TextField(max_length=20)
    core            = models.TextField(max_length=10)
    allocatedfor    = models.TextField(max_length=100)
    creationorder   = models.TextField(max_length=100)
    os              = models.TextField(max_length=40)
    License         = models.TextField(max_length=50)