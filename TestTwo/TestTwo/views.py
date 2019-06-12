from django.shortcuts import render

def home_page(request):
	title = "index"
	site_title = "Home Page"
	template = "index.html"
	return render(request,template,{"title":title,"site_title":site_title})