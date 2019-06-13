from django.shortcuts import render
import os
# Create your views here.

def command_view(request):
	output = os.popen('ls -l').read()
	return render(request,'output.html',{'output':output})