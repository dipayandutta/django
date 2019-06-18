from django.shortcuts import render

# Create your views here.
def home(request):
    templates = "design/home.html"
    title = "home"
    return render(request,templates,{'title':title})