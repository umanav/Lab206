# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses_app', '0002_auto_20180411_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
    ]