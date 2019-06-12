from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import BlogPost
# Create your views here.

# The slug value will be catch from the URL 
def blog_post_details_page(request,slug): 
	# check if the object exists or not
	obj 			= get_object_or_404(BlogPost,slug=slug)
	template_name 	= "blog/details.html"
	context			= {"object":obj,"title":"display","site_title":"blog details"}

	return render(request,template_name,context)


def blog_display_all(request):
	# get every thing from the database
	querySet 		= BlogPost.objects.all()
	template_name 	= "blog/display_blog.html"
	site_title		= "All Blogs"
	context			= {"object_list":querySet,"site_title":site_title}


	return render(request,template_name,context)