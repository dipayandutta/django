from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    #path('',index,name='index'),
    path('',views.allProdCat,name='allProdCat'),# all the products
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'), # all the products with matching Cat
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail,name='prodCatDetails')
]
