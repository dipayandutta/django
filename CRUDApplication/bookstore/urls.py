from django.urls import path
from .views import (
	HomePage,
	AddBook,
	Create,
	edit,
	delete,
	update,
	)
urlpatterns = [
	
	path('',HomePage),
	path('add/',AddBook),
	path('create/',Create),
	path('edit/<int:id>',edit),
	path('delete/<int:id>',delete),
	path('update/<int:id>',update)
]