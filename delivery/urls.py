from django.urls import path
from .import views

urlpatterns = [
    path('start-delivery/',views.start_delivery, name='start-delivery'),
    path('active-delivery/',views.active_delivery, name='active-delivery'),
    path('delivery-history/',views.delivery_history, name='delivery-histroy'),
    path('delivery-queue/',views.delivery_queue, name='delivery-queue'),
    path('accept-delivery/<str:serial_number>/', views.accept_delivery, name='accept-delivery'),
     path('reject-delivery/<str:serial_number>/', views.reject_delivery, name='reject-delivery'),
]
