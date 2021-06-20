from django.shortcuts import render,redirect

from .models import CountryData
from .forms import CountryDataForm

def index(request):
	template = 'dashboard/index.html'
	data = CountryData.objects.all()

	if request.method == 'POST':
		form = CountryDataForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = CountryDataForm()

	context = {

		'data': data,
		'form': form,
		'add_data': 'Add Data'
	}

	return render(request,template,context)