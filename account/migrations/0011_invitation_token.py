# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-18 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_invitation_login_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='token',
            field=models.CharField(default='e2bmldUhZXxGlg', max_length=64),
        ),
    ]
