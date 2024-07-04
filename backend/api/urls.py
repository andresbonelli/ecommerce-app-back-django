from django.urls import path
from . import views

urlpatterns = [
    # User paths
    path('', views.index, name="index"),
    path('products', views.products, name="products"),
    path('products/<int:id>', views.product_details, name="product_details"),
    path('update_stock/', views.update_stock, name='update_stock'),
    path('images/<int:image_id>/', views.get_product_image, name='get_product_image'),
    
]