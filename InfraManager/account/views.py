from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    template = 'accounts/home.html'
    title    = 'home'
    return render(request,template,{'title':title})


def index(request):
    template = 'accounts/index.html'
    title    = 'index'
    return render(request,template,{'title':title})

''' Signup View'''
def signup(request):
    template = 'accounts/signup.html'
    title    = 'signup'
    if request.method == 'POST':
        username        = request.POST['username']
        passwordFirst   = request.POST['password1']
        passwordSecond  = request.POST['password2']
        emailid         = request.POST['emailid']
        if passwordFirst == passwordSecond:
            try:
                user = User.objects.get(username=username)
                return render(request,template,{'error':'username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(username,password=passwordFirst,email=emailid)
                #auth.login(request,user)
                return render(request,template,{'message':'User Created Successfully'})
        else:
            return render(request,template,{'error':'password mismatch'})
    return render(request,template,{'title':title})

# Login View
def login(request):
    template = 'accounts/login.html'
    title    = 'login'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,template,{'error':'username or password mismatch'})
    return render(request,template,{'title':title})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')