# Generated by Django 3.1.7 on 2021-06-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0009_surat_jenis_surat'),
    ]

    operations = [
        migrations.AddField(
            model_name='penduduk',
            name='desa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]