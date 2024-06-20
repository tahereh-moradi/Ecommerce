from django.contrib import admin
from django.urls import path, include
#from shop.views import *

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('checkout/', checkout),
    path('product/', product),
    path('store/', store),
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("website.urls", namespace="website")),
    path('shop/', include("shop.urls", namespace="shop")),
]