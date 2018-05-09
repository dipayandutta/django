from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# A Many TO Many Relation Example Class

class Language(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name
        
# Relationship
class Programmer(models.Model):
    name = models.CharField(max_length= 20)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language) # Pass the Class 
    def __str__(self):
        return self.name

