from django.shortcuts import render,redirect
from .models import LogBook
# Create your views here.
def index(request):
    return render(request,"index.html",{})

def showlog(request):
    title = "showlog"
    template = "showlog.html"
    logs  = LogBook.objects.all()
    return render(request,template,{"title":title,"logs":logs})

def addlog(request):
    title = "addlogs"
    template = "addlog.html"

    return render(request,template,{"title":title})

def Create(request):

    author      = request.GET['author']
    designation = request.GET['designation']
    subject     = request.GET['subject']
    
    print(author)
    print (designation)
    print (subject)

    logs_to_store = LogBook(Author=author,Designation=designation,Subject=subject)
    logs_to_store.save()

    return redirect('/')