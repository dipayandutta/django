from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
	title = "This is the Home Page"
	return render(request,"home.html",{"site_title":"home","title":title})

