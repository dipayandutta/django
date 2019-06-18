from django.urls import path 
from .views import (
    signup,
    login,
    signout,
    user
    )

urlpatterns = [
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
    path('signout/',signout,name="signout"),
    path('user/',user,name='user'),
]
