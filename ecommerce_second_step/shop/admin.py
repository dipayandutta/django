from django.contrib import admin
from .models import Category,Products
# Register your models here.
#admin.site.register(Category)
#admin.site.register(Products)

class CategoryAdmin(admin.ModelAdmin):
    list_display            = ['name','slug']
    prepopulated_fields     = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display        = ['name','price','stock','available','created','update']
    list_editable       = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page       = 20
admin.site.register(Products,ProductAdmin)