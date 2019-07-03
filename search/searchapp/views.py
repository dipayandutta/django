from django.shortcuts import render,HttpResponseRedirect
from .models import Student
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def index(request):
    results = Student.objects.all()
    return render(request,"index.html",{'results':results})

def search(request):
    template = "search.html"
    title    = "search"
    if request.method == 'POST':
        srch = request.POST['srh']
        print(srch)

        if srch:
            match = Student.objects.filter(Q(name__icontains=srch) |
                                           Q(city__icontains=srch))
            print (match)
            if match:
                return render(request,template,{'sr':match})
            else:
                messages.error(request,'no result found!')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,template,{'title':title})

