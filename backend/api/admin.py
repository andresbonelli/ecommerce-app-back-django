from django.contrib import admin
from .models import Image, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'storage', 'carbs', 'fat', 'protein', 'salt', 'price', 'stock']
    search_fields = ['name', 'description', 'price']

admin.site.register(Image)
admin.site.register(Producto, ProductoAdmin)