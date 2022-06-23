from django.contrib import admin
from .models import Category, Product
# Register your models here.


admin.site.site_header='E-Commerce Admin'
admin.site.site_title='E-Commerce Admin'


admin.site.register(Category)
admin.site.register(Product)

