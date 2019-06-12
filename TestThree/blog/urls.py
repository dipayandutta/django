from django.urls import path

from .views import (
	blog_post_details_page,
	blog_display_all,
	)

urlpatterns = [
	#path('',blog_home),
	path('<str:slug>/',blog_post_details_page),
	path('',blog_display_all),
]