# Generated by Django 3.1.7 on 2021-05-29 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0004_sku'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sku',
            options={'verbose_name_plural': 'Sku'},
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='no',
        ),
    ]
