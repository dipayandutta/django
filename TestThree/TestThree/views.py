from django.shortcuts import render

def home_page(request):

	template = "home.html"
	title    = "index"
	site_title= "Home Page"

	return render(request,template,{"title":title,"site_title":site_title})