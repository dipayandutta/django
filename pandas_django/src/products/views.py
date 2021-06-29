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
	product_df['product_id'] = product_df['id']

	'''
	Mergind to Dataframe
	'''
	df = pd.merge(purchase_df,product_df,on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis=1)
	context  = {
		'products':product_df.to_html(),
		'purchase':purchase_df.to_html(),
		'df' : df.to_html()

	}
	return render(request,'products/main.html',context)