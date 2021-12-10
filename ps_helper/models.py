from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.shortcuts import render
from django.urls import reverse
from django.core.files.base import ContentFile, File
from django.contrib.auth.models import Group, Permission, ContentType
from django.utils import timezone
from django.core.validators import FileExtensionValidator


import os
import datetime


class TypeProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)

    class Meta:
        managed = True
        db_table = 'g_type'
        verbose_name = 'Тип товара'
        default_permissions = ()

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)

    class Meta:
        managed = True
        db_table = 'g_status'
        verbose_name = 'Статус'
        default_permissions = ()

    def __str__(self):
        return f"{self.name}"



class Product(models.Model):
    site_id = models.CharField(max_length=100, unique=True, verbose_name='ид стим')
    name = models.CharField(max_length=5000, verbose_name='Название')
    isExclusive = models.BooleanField(verbose_name='эксклюзив для ps')
    isFree = models.BooleanField(verbose_name='бесплатно')

    type_product = models.ForeignKey('TypeProduct', models.DO_NOTHING)
    status = models.ForeignKey('Status', models.DO_NOTHING)
    service_branding = models.ForeignKey('TypeUpsellServiceBranding', models.DO_NOTHING, null=True)
    
    date_add = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    class Meta:
        managed = True
        db_table = 'g_game'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        default_permissions = ()

    def __str__(self):
        return f"{self.name}"

    def last_price(self):
        return self.price_set.all().latest('date_add')
    
    def main_img(self):
        return self.media_set.all().earliest('date_add')


#### игра\платформа
class TypePlatform(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)

    class Meta:
        managed = True
        db_table = 'g_platform'
        verbose_name = 'Платформа'
        default_permissions = ()

    def __str__(self):
        return f"{self.name}"

class ProductPlatform(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    platform = models.ForeignKey('TypePlatform', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'g_product_platform'
        unique_together = (('product', 'platform'), )
        verbose_name = 'Платформа игры'
        default_permissions = ()

    def __str__(self):
        return f"{self.product} {self.platform}"



class TypeUpsellServiceBranding(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)

    class Meta:
        managed = True
        db_table = 'g_type_upsell_service_branding'
        verbose_name = 'Подписка'
        default_permissions = ()

    def __str__(self):
        return f"{self.name}"


# скидка по подписке
class UpsellServiceBranding(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    type = models.ForeignKey('TypeUpsellServiceBranding', models.DO_NOTHING)
    sale_text = models.CharField(max_length=100)
    date_add = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    class Meta:
        managed = True
        db_table = 'g_UpsellServiceBranding'
        verbose_name = 'Скидка по подписке'
        unique_together = (('product', 'type', 'sale_text'), )
        default_permissions = ()

    def __str__(self):
        return f"{self.text}"


class Media(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    type = models.CharField(max_length=50, verbose_name='Тип')
    url = models.CharField(max_length=255, unique=True)
    date_add = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    class Meta:
        managed = True
        db_table = 'g_medis'
        verbose_name = 'Медиа'
        default_permissions = ()

    def __str__(self):
        return f"{self.product} {self.type}"


class Price(models.Model):
    product = models.ForeignKey('Product', models.DO_NOTHING)
    base_price = models.CharField(max_length=50)
    discountText = models.CharField(max_length=50, null=True)
    discountedPrice = models.CharField(max_length=50, null=True)
    price_amount = models.IntegerField(verbose_name='Цена', null=True)
    discount_price_amount = models.IntegerField(verbose_name='Цена со скидкой', null=True)
    date_add = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    class Meta:
        managed = True
        db_table = 'g_price'
        verbose_name = 'Цены'
        default_permissions = ()
        unique_together = (('product', 'price_amount', 'discount_price_amount'), )

    def __str__(self):
        return f"{self.product} {self.base_price}"
