# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdb_store', '0003_auto_20181011_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]