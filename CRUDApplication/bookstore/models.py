from django.db import models

# Create your models here.
class BookStore(models.Model):

	title = models.TextField(max_length=140)
	price = models.IntegerField()
	author= models.TextField(max_length=200)