from django.shortcuts import render , redirect
#import database
from .models import BookStore
# Create your views here.
def HomePage(request):
	template  = "home.html"
	title     = "home"

	# create an object of the BookStore class 
	# Retrive all the data from the database

	books = BookStore.objects.all()
	return render(request,template,{"title":title,"books":books})


def AddBook(request):
	template	= "addbooks.html"
	title		= "add"
	return render(request,template,{"title":title})

def Create(request):
	print(request.POST)

	title = request.GET['title']
	price = request.GET['price']
	author= request.GET['author']

	print(title)
	print(price)
	print(author)

	# creating an object of BookStore Class
	BookLists = BookStore(title=title,price=price,author=author)
	# Save the datas in the database
	BookLists.save()
	# redirect to the home page
	return redirect('/')

def edit(request,id):
	books = BookStore.objects.get(pk=id)
	title = "edit"
	context = {
			'result':books
	}
	return render(request,'edit.html',context,{"title":title})

def delete(request,id):
	book = BookStore.objects.get(pk=id)
	book.delete()

	return redirect('/')

def update(request,id):
	books = BookStore.objects.get(pk=id)

	books.title = request.GET['title']
	books.price = request.GET['price']
	books.author= request.GET['author']

	books.save()
	return redirect('/')