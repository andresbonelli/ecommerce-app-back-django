from django.contrib import admin
from .models import Image, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'storage', 'carbs', 'fat', 'protein', 'salt', 'price', 'stock']
    search_fields = ['name', 'description', 'price']
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'image']
    
admin.site.register(Image, ImageAdmin)
admin.site.register(Producto, ProductoAdmin)