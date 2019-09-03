from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
# Create your views here.

def index(request):
	text_display = 'This is a sample Text for Testing'
	return HttpResponse(text_display)

# Creating all product view
def allProduct(request,c_slug=None):
	c_page 		= None
	products 	= None
	#check if it is a product based view
	# if yes
	if c_slug != None:
		# Try to get the object from the database or return 404 error 
		c_page 		= get_object_or_404(Category,slug=c_slug)
		products  = Product.objects.filter(category=c_page,available=True)
	else:
		# Else display all the products in the database
		products	= Product.objects.all().filter(available=True)
		
	return render(request,'shop/category.html',{'category':c_page,'products':products})

def productDetails(request,c_slug,product_slug):
	try:
		product = Product.objects.get(category__slug=c_slug,slug=product_slug)
	except Exception as e:
		raise e
	
	return render(request,'shop/product.html',{'product':product})
