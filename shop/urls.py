from django.urls import path, include
from .views import *


app_name = 'shop'

urlpatterns = [
    path('index/', index, name='index'),
    path('checkout/', checkout, name='checkout'),
    path('product/', product, name='product'),
    path('store/', store, name="store"),
]