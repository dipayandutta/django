from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    template = "home.html"
    title = "home"
    message = "This is the home page"
    return render(request,template,{"title":title,"message":message})