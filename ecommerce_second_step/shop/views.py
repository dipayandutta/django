from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Category,Products

# Create your views here.
def index(request):
    text_var = 'This is my First Django Web Application'
    return HttpResponse(text_var)


# Create Category View
def allProdCat(request,c_slug=None):
    c_page      = None
    products    = None
    if c_slug!=None:
        # Display the products based on the category
        # Check if the product exists 
        c_page      = get_object_or_404(Category,slug=c_slug)
        products    = Products.objects.filter(category=c_page,available=True)
    else:
        # Display all the products
        products    = Products.objects.all().filter(available=True)

    return render(request,'shop/category.html',{'category':c_page,'products':products})    

# Create the product view

def ProdCatDetail(request,c_slug,product_slug):
    # First check the product exists or not using try catch
    try:
        # If product exists using slug URL Then Display
        product = Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e 

    return render(request,'shop/product.html',{'product':product})