# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-05-07 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sni', '0006_auto_20180424_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetails',
            name='itemurl',
            field=models.CharField(default=b' ', max_length=300),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='itemimage',
            field=models.CharField(default=b' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='itemname',
            field=models.CharField(default=b' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='price',
            field=models.CharField(default=b' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='itemdetails',
            name='rating',
            field=models.CharField(default=b' ', max_length=200),
        ),
    ]
