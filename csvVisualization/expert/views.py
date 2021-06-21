from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
import os
from django.contrib import messages
import pandas as pd
from collections import Counter
# Create your views here.
def index(request):

	global attribute
	template = 'expert/index.html'

	if request.method == 'POST':
		upload_file = request.FILES['document']
		attribute = request.POST.get('attributeid')

		print(upload_file)
		print (attribute)

		if upload_file.name.endswith('.csv'):
			#save the file
			savefile = FileSystemStorage()
			name = savefile.save(upload_file.name,upload_file)

			project_dir = os.getcwd()
			file_dir = project_dir+'/media/'+name
			readfile(file_dir)

			return redirect(result)
		else:
			messages.warning(request,'Files Was not uploaded, Please use CSV extension!')
			
	return render(request,template)


def readfile(filename):

	global rows,columns,data,my_file,missing_vlaues
	my_file = pd.read_csv(filename,sep='[:;,|_]', engine='python')
	data = pd.DataFrame(data=my_file,index=None)
	print(data)

	# getting rows and columns
	rows = len(data.axes[0])
	columns = len(data.axes[1])


	# find the missing data
	missingSigns = ['?','0','--','-',' ']
	null_data = data[data.isnull().any(axis=1)]
	missing_vlaues = len(null_data)

def result(request):
	template = 'expert/result.html'

	message = 'Data Details '+str(rows)+'x'+str(columns)+' Missing Data '+str(missing_vlaues)
	messages.warning(request,message)

	# split data into keyes and values attribute

	dashboard = []

	for x in data[attribute]:
		dashboard.append(x)

	my_dashboard = dict(Counter(dashboard))
	print(my_dashboard)

	keys = my_dashboard.keys()
	values = my_dashboard.values()

	listkeys = []
	listvalues = []

	for x in keys:
		listvalues.append(x)

	for y in values:
		listvalues.append(y)

	context = {

		'listkeys': listkeys,
		'listvalues':listvalues

	}

	return render(request,template,context)