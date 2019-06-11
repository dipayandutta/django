from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title 		= models.TextField()
	content		= models.TextField(null=True,blank=True)
	author  	= models.CharField(max_length=30,default="Name")
	CreationTime= models.DateTimeField(null=True)