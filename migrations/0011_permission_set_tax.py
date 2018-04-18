# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-08 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0010_list_of_bug_client_api_bug'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission_set',
            name='tax',
            field=models.IntegerField(choices=[(0, 'No Permission'), (1, 'Read Only'), (2, 'Edit Only'), (3, 'Add and Edit'), (4, 'Full Permission')], default=0),
        ),
    ]