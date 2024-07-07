from django.urls import path
from . import views

urlpatterns = [
# Authorized admin paths
    path('products/', views.ProductListCreate.as_view(), name="admin_product_list"),
    path('products/update/<int:id>/', views.ProductUpdate.as_view(), name="admin_update_product"),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name="admin_product_delete"),
    path('images/', views.ImageListCreate.as_view(), name="admin_image_list")
]   