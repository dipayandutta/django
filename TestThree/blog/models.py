from django.db import models

# Create your models here.
class BlogPost(models.Model):

	title 		= models.TextField(null=True)
	author		= models.TextField(null=True)
	content 	= models.TextField(null=True)
	created_at	= models.DateTimeField(null=True)
	slug 		= models.SlugField(unique=True) # This is used to take as an argument in the URL
	

