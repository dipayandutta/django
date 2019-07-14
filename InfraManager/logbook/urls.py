from django.urls import path
from .views import (
    addlog,
    Create,
    showlog
)

urlpatterns = [
    path('add/',addlog,name='addlog'),
    path('create/',Create,name='create'),
    path('showlogs/',showlog,name='showlog')
]
