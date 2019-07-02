from django.shortcuts import render

# Create your views here.
def addservers(request):
    template = "addservers.html"
    return render(request,template,{})