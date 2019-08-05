from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email= form.cleaned_data['email']
            category = form.cleaned_data['category']
            print (name)
            print (email)
            print (category)
    template='form.html'
    form = ContactForm()
    return render(request,template,{'form':form})
    #return HttpResponse('Contact View')