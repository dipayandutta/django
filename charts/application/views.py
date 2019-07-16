from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def index(request):
    template='charts.html'
    return render(request,template,{'customers':10})

def get_date(request):
    data = {
        "sales":100,
        "customers":10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes  = []
    permission_classes      = []

    def get(self,request,format=None):
        labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default = [10,20,30,5,40,20]
        data = {
                "labels":labels,
                "default":default,
        }
        return Response(data)