from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import LogBookEntry
# Create your views here.

@login_required
def addlog(request):
    template = 'logs/addlog.html'
    title = 'Log Entry'
    return render(request,template,{'title':title})

@login_required
def Create(request):
    
    author          = request.GET['author']
    designation     = request.GET['designation']
    subject         = request.GET['subject']
    reportedto      = request.GET['reportedto']
    instructedby    = request.GET['instructedby']
    '''
    print(author)
    print(designation)
    print(subject)
    print(reportedto)
    print (instructedby)
    '''
    log_to_store = LogBookEntry(Author=author,Designation=designation,Subject=subject,ReportedTo=reportedto,InstructedBy=instructedby)
    log_to_store.save()

    return redirect('addlog')

@login_required
def showlog(request):
    title = 'showlog'
    template = 'logs/showlogs.html'
    logs     = LogBookEntry.objects.all()
    return render(request,template,{'title':title,"logs":logs})