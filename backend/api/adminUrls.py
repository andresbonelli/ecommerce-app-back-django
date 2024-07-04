from django.urls import path
from . import views

urlpatterns = [
# Authorized admin paths
    path('products/', views.ProductListCreate.as_view(), name="admin_product_list"),
    path('products/delete/<int:id>/', views.ProductDelete.as_view(), name="admin_product_delete")
]   