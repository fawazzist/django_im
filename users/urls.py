from django.urls import path
from . import views

urlpatterns = [
    path('register_purchaser/',views.register_purchaser, name='register-purchaser'),
    path('register_warehouse/',views.register_warehouse, name='register-warehouse'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
]
