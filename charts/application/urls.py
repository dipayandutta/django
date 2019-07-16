from django.urls import path
from .views import index,get_date,ChartData
urlpatterns = [
    path('',index,name='index'),
    path('api/data',get_date,name='api-data'),
    path('api/chart/data',ChartData.as_view()),
]
