from django.urls import path
from .views import (
    index,
    signup,
    login,
    home,
    logout
)
urlpatterns = [
    path('',index,name='index'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('home/',home,name='home'),
    path('logout/',logout,name='logout')
]
