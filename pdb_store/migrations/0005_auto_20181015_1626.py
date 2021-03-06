# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdb_store', '0004_auto_20181011_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_items', to='pdb_store.Author')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.TextField()),
                ('feed_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_parts', to='pdb_store.FeedItem')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.RemoveField(
            model_name='letter',
            name='author',
        ),
        migrations.RemoveField(
            model_name='page',
            name='letter',
        ),
        migrations.DeleteModel(
            name='Letter',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
