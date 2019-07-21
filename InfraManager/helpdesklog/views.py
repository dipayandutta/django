from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import HelpDesk
# Create your views here.
@login_required
def addlog(request):
    template = 'AddLogs.html'
    title = 'add logs'
    return render(request,template,{'title':title})

@login_required   
def showlog(request):
    template = 'showlogs.html'
    title = 'logs'
    helpdesklogs = HelpDesk.objects.all()
    paginator = Paginator(helpdesklogs,5)
    page = request.GET.get('page')
    helpdesklogs = paginator.get_page(page)
    return render(request,template,{'title':title,'logs':helpdesklogs})

@login_required
def createlog(request):
    hdshift         = request.GET['hdshift']
    callfrom        = request.GET['callfrom']
    problemtype     = request.GET['problemtype']
    contactperson   = request.GET['contactperson']
    solutionstatus  = request.GET['solutionstatus']
    remarks         = request.GET['remarks']

    print(hdshift)
    print(callfrom)
    print(problemtype)
    print(contactperson)
    print(solutionstatus)
    print(remarks)

    helpdesk_data = HelpDesk(HDShift=hdshift,CallFrom=callfrom,ProblemType=problemtype,CnctPerson=contactperson,SolvedStatus=solutionstatus,Remarks=remarks)
    helpdesk_data.save()

    return redirect('addhelpdesklog')