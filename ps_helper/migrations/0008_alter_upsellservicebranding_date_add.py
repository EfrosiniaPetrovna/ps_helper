# Generated by Django 3.2.7 on 2021-10-10 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ps_helper', '0007_alter_upsellservicebranding_date_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upsellservicebranding',
            name='date_add',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
