from django.contrib import admin
from .models import Product, Category
# Register your models here.

class productAdmin(admin.ModelAdmin):
    pass

class categoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, productAdmin)
admin.site.register(Category, productAdmin)

