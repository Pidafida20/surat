# Generated by Django 3.1.7 on 2021-08-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0030_auto_20210802_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penduduk',
            name='nik',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
