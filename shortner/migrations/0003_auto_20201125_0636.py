# Generated by Django 3.1.3 on 2020-11-25 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_auto_20201125_0340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UrlMappings',
            new_name='UrlMapping',
        ),
    ]
