from django.shortcuts import render
import os
# Create your views here.

def command_view(request):
    os.chdir('/code/python/paramiko')
    result = os.popen('python exampleTwo.py').read()
    return render(request,'output.html',{'result':result})