# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-19 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
