# Generated by Django 3.2.7 on 2021-09-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps_helper', '0002_auto_20210923_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='price',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='upsellservicebranding',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
