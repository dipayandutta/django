from django import forms
from .models import Purchases , Product

class PurchaseForm(forms.ModelForm):
	product = forms.ModelChoiceField(queryset=Product.objects.all(),label=
		'Product',widget=forms.Select(attrs={'class':'ui selection dropdown field-width'}))
	class Meta:
		model 	= Purchases
		fields 	= ['product','price','quantity'] 