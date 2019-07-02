from django.urls import path
from .views import (
    index,
    showlog,
    addlog,
    Create
)

urlpatterns = [
    path('',index,name='home'),
    path('showlogs/',showlog,name='showlog' ) ,
    path('addlogs/',addlog,name='addlog'),
    path('create/',Create,name='create')
]
