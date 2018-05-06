from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.index,name='index'),
    path('user/',views.user,name='user')
]