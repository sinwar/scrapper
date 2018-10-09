# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-04-24 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sni', '0004_addthing'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(default=' ', max_length=30)),
                ('itemimage', models.ImageField(default=' ', upload_to='/home/sinwar/djcode/itemdetails/sni/site_media/media/things/')),
                ('price', models.FloatField()),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='addthing',
            name='sound',
            field=models.FileField(default=' ', upload_to='/home/sinwar/djcode/itemdetails/sni/site_media/media/sounds/'),
        ),
        migrations.AlterField(
            model_name='addthing',
            name='soundimage',
            field=models.ImageField(default=' ', upload_to='/home/sinwar/djcode/itemdetails/sni/site_media/media/things/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=' ', upload_to='/home/sinwar/djcode/itemdetails/sni/site_media/media'),
        ),
    ]