# Generated by Django 3.1.7 on 2021-05-31 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0005_auto_20210529_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sku',
            name='no',
        ),
    ]
