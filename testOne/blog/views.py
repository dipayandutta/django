from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def blog_post_results(request,post_id):
	obj 			= BlogPost.objects.get(id=post_id)
	template_name	= "blogs.html"
	context			={"object":obj}

	return render(request,template_name,context,{"site_title":"results","title":"Display Blogs"})