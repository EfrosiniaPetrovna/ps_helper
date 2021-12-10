from .models import *
from rest_framework import serializers


class TypeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class UpsellServiceBrandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpsellServiceBranding
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    type_product = TypeProductSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    service_branding = UpsellServiceBrandingSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


