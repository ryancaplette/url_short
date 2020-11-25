# Generated by Django 3.1.3 on 2020-11-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_path', models.CharField(max_length=6)),
                ('original_url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]