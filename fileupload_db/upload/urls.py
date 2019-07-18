from django.urls import path
from .views import index,upload,upload_book,book_list,delete_book

urlpatterns = [
    path('',index,name='index'),
    path('upload/',upload,name='upload'),
    path('books/',book_list,name='book_list'),
    path('books/upload/',upload_book,name='upload_books'),
    path('books/<int:pk>/',delete_book,name='delete_book')
]
