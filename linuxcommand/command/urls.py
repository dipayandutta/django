from django.urls import path
from .views import (
	command_view
	) 

urlpatterns = [
	path('',command_view,name="display result")
]