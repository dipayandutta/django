from django.db import models

# Create your models here.
class Sinppet(models.Model):
    name = models.CharField(max_length=180)
    body = models.TextField()

    def __str__(self):
        return self.name