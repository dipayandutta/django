from django.urls import path

from . views import (
	blog_display
	)

urlpatterns = [
	path('',blog_display),
]