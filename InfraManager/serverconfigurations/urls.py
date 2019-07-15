from django.urls import path
from .views import (
    ShowServerLists,
    ShowServerDetails,
    AddServers,
    CreateServerLists,
    EditServers,
    UpdateServerDetails,
    DeleteServerRecord
)
urlpatterns = [
    path('lists/',ShowServerLists,name='serverslists'),
    path('details/',ShowServerDetails,name='serverdetails'),
    path('addservers/',AddServers,name='addservers'),
    path('create/',CreateServerLists,name='Create'),
    path('editservers/<int:SerialNumber>/',EditServers,name='editservers'),
    path('updateservers/<int:SerialNumber>/',UpdateServerDetails,name='updateservers'),
    path('deleteserver/<int:SerialNumber>/',DeleteServerRecord,name='deleteserver'),
]
