# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-19 11:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='puplised_date',
            new_name='puplished_date',
        ),
    ]
