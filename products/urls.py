from django.urls import path
from .import views


urlpatterns = [
    path('add-product/', views.add_product, name='add-product'),
    path('products-dashboard/', views.product_list, name='products-dashboard'),
  
]
