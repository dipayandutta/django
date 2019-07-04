from django.urls import path
from .views import (
    home,
    delete,
    cross_off,
    uncross,
    )

urlpatterns = [
    path('',home,name='home'),
    path('delete/<list_id>',delete,name='delete'),
    path('cross_off/<list_id>',cross_off,name="cross_off"),
    path('uncross/<list_id>',uncross,name="uncross"),
]
