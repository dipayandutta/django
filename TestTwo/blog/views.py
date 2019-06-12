from django.shortcuts import render

# Create your views here.
def blog_display(request):
	title = "blog"
	site_title = "Blogs"
	template = "blog/display.html"

	return render(request,template,{"title":title,"site_title":site_title})