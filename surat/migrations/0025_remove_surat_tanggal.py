# Generated by Django 3.1.7 on 2021-07-28 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0024_auto_20210728_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surat',
            name='tanggal',
        ),
    ]
