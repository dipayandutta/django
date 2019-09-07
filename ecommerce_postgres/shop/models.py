from django.db import models
from django.urls import reverse

# Create your models here.
# Creating the Category Model
class Category(models.Model):
	name 				= models.CharField(max_length=250,unique=True)
	slug 				= models.SlugField(max_length=250,unique=True)
	description	= models.TextField(blank=True)
	image 			= models.ImageField(upload_to='category',blank=True)
	
	class Meta:
		ordering 						= ('name',)
		verbose_name				= 'category'
		verbose_name_plural	= 'categories'
		
	# creating a get_url method for navigation and argument passing to views file
	def get_url(self):
		return reverse('shop:products_by_category',args=[self.slug])
	
	def __str__(self):
		return '{}'.format(self.name)
		
# Creating the Product Model
class Product(models.Model):
	name 				= models.CharField(max_length=250,unique=True)
	slug				= models.SlugField(max_length=250,unique=True)
	description	= models.TextField(blank=True)
	category		= models.ForeignKey(Category,on_delete=models.CASCADE)
	price				= models.DecimalField(max_digits=10,decimal_places=2)
	image				= models.ImageField(upload_to='product',blank=True)
	stock 			= models.IntegerField()
	available		= models.BooleanField(default=True)
	created			= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	
	
	class Meta:
		ordering					=('name',)
		verbose_name			='product'
		verbose_name_plural= 'products'

	# creating a get_url method for navigation and argument passing to views file
	def get_url(self):
		return reverse('shop:prodCatDetails',args=[self.category.slug,self.slug])
	
	def __str__(self):
		return '{}'.format(self.name)