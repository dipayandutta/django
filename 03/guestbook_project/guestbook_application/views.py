from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'guestbook/index.html')

def sign(request):
    return render(request,'guestbook/sign.html')