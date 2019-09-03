# This is python script to display all the menu itmes 
from .models import Category
# Method name 
def menu_links(request):
	links = Category.objects.all() # Reading all the categories from the database
	return dict(links=links) # Return them as a dictonary item

# This is dict will uncover in the navbar.html section 
