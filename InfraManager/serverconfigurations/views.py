from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from subprocess import Popen , PIPE
from .models import ServerDetails
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def ShowServerLists(request):
   
    template = 'servers/servers.html'
    title = 'servers'
    output=[]
    
    # get all the ip address from the database in an array format
    ipaddress = ServerDetails.objects.values_list('ipaddress',flat=True)
    for ip in ipaddress:
        print(ip)
        ip = str(ip)
        hoststatus = Popen(["ping","-c2",ip],stdout=PIPE)
        result = hoststatus.communicate()[0]
        ret_code = hoststatus.returncode

        if ret_code == 0:
            output.append("UP {0}".format(ip))
        else:
            output.append("DOWN {0}".format(ip))
    #print(ipaddress)
    
    return render(request,template,{'title':title,'output':output})

@login_required(login_url='/login/')
def ShowServerDetails(request):
    template='servers/ShowDetails.html'
    title = 'servers'
    servers = ServerDetails.objects.all()
    paginator = Paginator(servers,5)
    page = request.GET.get('page')
    servers = paginator.get_page(page)
    return render(request,template,{'title':title,'servers':servers})

@login_required(login_url='/login/')
def AddServers(request):
    title = 'add servers'
    template='servers/AddLists.html'
    return render(request,template,{'title':title})

@login_required(login_url='/login/')
def CreateServerLists(request):

    ipaddress   = request.GET['ipaddress']
    hdd         = request.GET['hdd']
    ram         = request.GET['ram']
    core        = request.GET['core']
    allocatedfor= request.GET['allocatedfor']
    creationorder=request.GET['creationorder']
    os          = request.GET['os']
    License     = request.GET['License']

   
    store_servers = ServerDetails(ipaddress=ipaddress,hdd=hdd,ram=ram,core=core,allocatedfor=allocatedfor,creationorder=creationorder,os=os,License=License)
    store_servers.save()

    return redirect('addservers')

@login_required(login_url='/login/')
def EditServers(request,SerialNumber):
    server = ServerDetails.objects.get(pk=SerialNumber)
    template = 'servers/edit.html'
    title = 'edit servers'
    return render(request,template,{'title':title,'server':server})

@login_required(login_url='/login/')
def UpdateServerDetails(request,SerialNumber):
    server = ServerDetails.objects.get(pk=SerialNumber)

    server.ipaddress    = request.GET['ipaddress']
    server.hdd          = request.GET['hdd']
    server.ram          = request.GET['ram']
    server.core         = request.GET['core']
    server.allocatedfor = request.GET['allocatedfor']
    server.creationorder= request.GET['creationorder']
    server.os           = request.GET['os']
    server.License      = request.GET['License']

    server.save()
    return redirect('serverdetails') 

@login_required(login_url='/login/')
def DeleteServerRecord(request,SerialNumber):
    server  = ServerDetails.objects.get(pk=SerialNumber)
    server.delete()

    return redirect('serverdetails')