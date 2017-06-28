# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 14:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='papers', to=settings.AUTH_USER_MODEL),
        ),
    ]