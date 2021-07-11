from django.shortcuts import render
from .models import Product,Purchases
import pandas as pd
from .utils import get_simple_plot
# Create your views here.

def chart_select_view(request):
	'''
	qs1 = Product.objects.all().values()
	qs2 = Product.objects.all().values_list()
	print (qs1)
	print (qs2)
	'''
	graph = None
	error_message = None
	df = None
	price = None
	product_df = pd.DataFrame(Product.objects.all().values())
	purchase_df= pd.DataFrame(Purchases.objects.all().values())
	#print(product_df)
	product_df['product_id'] = product_df['id']
	'''
		Checking the existance of the data in the
		Database using pandas shape object
	'''
	if purchase_df.shape[0] >0:
		#print(purchase_df.shape)
		'''
			Merging to Dataframe
		'''
		df = pd.merge(purchase_df,product_df,on='product_id').drop(['id_y','date_y'],axis=1).rename({'id_x':'id','date_x':'date'},axis=1)
		price = df['price']


		#printing date
		#print(df['date'][0])
		#print(type(df['date'][0]))
		'''
			Getting the form data
		'''
		if request.method == 'POST':
			
			chart_type = request.POST['sales']
			date_form  = request.POST['date_form']
			date_to    = request.POST['date_to']
			print("chart "+chart_type)

			df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
			#print(df['date'])

			df2 = df.groupby('date',as_index=False)['total_price'].agg('sum')
			#print(df2)

			#print(chart_type+'-->'+date_form+'-->'+date_to)

			if chart_type!="":
				if date_form != "" and date_to !="":
					df = df[(df['date']>date_form) & (df['date']<date_to)] 
					df2 = df.groupby('date',as_index=False)['total_price'].agg('sum')
					print(df2)
				#Function to get a graph
				graph = get_simple_plot(chart_type,x=df2['date'],y=df2['total_price'],data=df)
					
			else:
				error_message = "Please select a chart type to Continue!"
	
	

	else:
		error_message='No Records in the Database!'
		

	

	context  = {
		'graph':graph,
		'price':price,
		'error_message':error_message,
		#'products':product_df.to_html(),
		#'purchase':purchase_df.to_html(),
		#'df' : df,

	}
	return render(request,'products/main.html',context)