# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-03 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]