# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-04-24 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sni', '0005_auto_20180424_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetails',
            name='itemimage',
            field=models.CharField(default=b' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='itemname',
            field=models.CharField(default=b' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='price',
            field=models.CharField(default=b' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='rating',
            field=models.CharField(default=b' ', max_length=50),
        ),
    ]