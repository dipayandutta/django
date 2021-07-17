from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from products.models import Product,Purchases
# Create your views here.
def upload_file_view(request):
	form = CsvForm(request.POST or None,request.FILES or None)
	add_message 	= None
	error_message	= None
	if form.is_valid():
		form.save()

		form = CsvForm()

		obj  = Csv.objects.get(activated=False)
		with open(obj.file_name.path,'r') as f:
			reader = csv.reader(f)

			for row in reader:
				row = "".join(row)
				row = row.replace(';',' ')
				row = row.split()
				

				user = User.objects.get(id=row[3])
				print(user)
				#populating Products database 
				prod,_ = Product.objects.get_or_create(name=row[0])
				#Populating Purchase Database
				Purchases.objects.create(
					product = prod ,
					price  	=int(row[2]),
					quantity=int(row[1]),
					salesman=user,
					date    =row[4]+" "+row[5]
					)

		obj.activated = True 
		obj.save()

		add_message = 'File Uploaded'


	context = {
		'form':form,
		'add_message':add_message,
	}
	return render(request,'csvs/upload.html',context)