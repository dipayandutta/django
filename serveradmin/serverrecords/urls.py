from django.urls import path 
from .views import addservers
urlpatterns = [
    path('add/',addservers,name='addservers')
]
