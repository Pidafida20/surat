# Generated by Django 3.1.7 on 2021-07-28 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0025_remove_surat_tanggal'),
    ]

    operations = [
        migrations.AddField(
            model_name='surat',
            name='tanggal',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
