from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    template='index.html'
    return render(request,template,{})

def upload(request):
    template = 'upload.html'
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
        #print(uploaded_file.name)
        #print(uploaded_file.size)
    return render(request,template,context)