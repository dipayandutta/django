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

	error_message = None
	df = None
	product_df = pd.DataFrame(Product.objects.all().values())
	purchase_df= pd.DataFrame(Purchases.objects.all().values())
	#print(product_df)
	product_df['product_id'] = product_df['id']
	'''
		Checking the existance of the data in the
		Database using pandas shape object
	'''
	if purchase_df.shape[0] >0:
		print(purchase_df.shape)
		'''
			Merging to Dataframe
		'''
		df = pd.merge(purchase_df,product_df,on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis=1)
		'''
			Getting the form data
		'''
		if request.method == 'POST':
			
			chart_type = request.POST['sales']
			date_form  = request.POST['date_form']
			date_to    = request.POST['date_to']

			print(chart_type+'-->'+date_form+'-->'+date_to)
	
	

	else:
		error_message='No Records in the Database!'
		

	

	context  = {
		'error_message':error_message,
		#'products':product_df.to_html(),
		#'purchase':purchase_df.to_html(),
		#'df' : df,

	}
	return render(request,'products/main.html',context)