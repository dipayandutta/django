from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book

# Create your views here.
def index(request):
    template = 'index.html'
    return render(request,template,{})

def upload(request):
    template = 'upload.html'
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    return render(request,template,context)

def book_list(request):
    template = 'book_list.html'
    books = Book.objects.all()
    return render(request,template,{'books':books})

def upload_book(request):
    template = 'upload_book.html'
    
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,template,{'form':form})

def delete_book(request,pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')