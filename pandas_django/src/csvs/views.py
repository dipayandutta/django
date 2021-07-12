from django.shortcuts import render
from .forms import CsvForm
# Create your views here.
def upload_file_view(request):
	form = CsvForm(request.POST or None,request.FILES or None)
	add_message = None

	if form.is_valid():
		obj = form.save()

		form = CsvForm()
		add_message = 'File Uploaded'

	context = {
		'form':form,
		'add_message':add_message,
	}
	return render(request,'csvs/upload.html',context)