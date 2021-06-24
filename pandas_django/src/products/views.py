from django.shortcuts import render
from .models import Product,Purchases
import pandas as pd
# Create your views here.

def chart_select_view(request):
	'''
	qs1 = Product.objects.all().values()
	qs2 = Product.objects.all().values_list()
	print (qs1)
	print (qs2)
	'''
	product_df = pd.DataFrame(Product.objects.all().values())
	purchase_df= pd.DataFrame(Purchases.objects.all().values())
	print(product_df)
	context  = {
		'products':product_df.to_html(),
		'purchase':purchase_df.to_html(),

	}
	return render(request,'products/main.html',context)