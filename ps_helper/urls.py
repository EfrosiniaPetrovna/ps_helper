from django.urls import path, include
from .views import *

from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'products/', Products)


urlpatterns = [
    #path('products/', Products, name='products'),
]

urlpatterns += router.urls