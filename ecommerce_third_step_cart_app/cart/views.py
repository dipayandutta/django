from django.shortcuts import render

# Create your views here.
# Three tasks to perform in this application
# No-01. If session ID is created on the users browser
# No-02. - Add product on the shopping cart 
# No-03. - Display items on the shopping cart

def __cart_id(request):
    cart = request.session.session_key