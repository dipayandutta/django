from django.urls import path 
from .views import showlog,addlog,createlog
urlpatterns = [
    path('showlog/',showlog,name='showhelpdesklog'),
    path('addlog/',addlog,name='addhelpdesklog'),
    path('create/',createlog,name='create'),
]
