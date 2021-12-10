import json

from django.shortcuts import render, redirect, HttpResponseRedirect, render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from django.db.models import Max, Count, Sum
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views import generic


from .models import *

# manage.py runserver_plus --print-sql


from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from rest_framework import viewsets
from .serializers import *


class Products(viewsets.ModelViewSet):
    queryset = Product.objects.filter(id__lte=10).order_by('-id')
    serializer_class = ProductSerializer
    


# def get_products(request):
#     products = Product.objects.all().select_related('type_product')
    
#     data = [
#         {'pk':i.id, 'name':i.name, 'type':i.type_product.name, 
#         'isExclusive':i.isExclusive, 'isFree':i.isFree, } for i in products]
#     data = json.dumps(data)
#     #data = serializers.serialize("json", [products, type_product])
#     return JsonResponse(data, safe=False)

