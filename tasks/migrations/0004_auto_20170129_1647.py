# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20170129_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
