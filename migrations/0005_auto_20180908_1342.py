# Generated by Django 2.1 on 2018-09-08 13:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0004_auto_20180906_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_history',
            name='contact_history',
            field=tinymce.models.HTMLField(verbose_name='contact_history'),
        ),
    ]
