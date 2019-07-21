from django.db import models
from django.utils import timezone
# Create your models here.

class HelpDesk(models.Model):
    SerialNumber = models.AutoField(primary_key=True)
    Date         = models.DateField(default=timezone.now)
    HDShift      = models.TextField(max_length=20)
    CallFrom     = models.TextField(max_length=50)
    ProblemType  = models.TextField(max_length=100)
    CnctPerson   = models.TextField(max_length=30)
    SolvedStatus = models.TextField(max_length=10)
    Remarks      = models.TextField(max_length=200)
