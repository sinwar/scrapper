# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-17 00:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sni', '0003_auto_20170416_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='addThing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soundname', models.CharField(default=' ', max_length=30)),
                ('soundimage', models.ImageField(default=' ', upload_to='/home/sinwar/djcode/sni/sni/site_media/media/things/')),
                ('sound', models.FileField(default=' ', upload_to='/home/sinwar/djcode/sni/sni/site_media/media/sounds/')),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='owneruser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]