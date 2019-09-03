from django.urls import path
from .views import index,allProduct,productDetails

app_name = 'shop'

urlpatterns = [
	#path('',index,name='index'),
	# Display all the products in the store
	path('',allProduct,name='allProduct'),
	#Display porudct by category
	path('<slug:c_slug>/',allProduct,name='products_by_category'),
	path('<slug:c_slug>/<slug:product_slug>/',productDetails,name='prodCatDetails')
	]
