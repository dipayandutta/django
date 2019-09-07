from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import Category,Products
# For pagination
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def index(request):
    text_var = 'This is my First Django Web Application'
    return HttpResponse(text_var)


# Create Category View
def allProdCat(request,c_slug=None):
    c_page      = None
    products_list    = None
    if c_slug!=None:
        # Display the products based on the category
        # Check if the product exists 
        c_page      = get_object_or_404(Category,slug=c_slug)
        products_list    = Products.objects.filter(category=c_page,available=True)
    else:
        # Display all the products
        products_list    = Products.objects.all().filter(available=True)
    # paginator code
    paginator = Paginator(products_list,6) # number of item in each page is 6
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
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