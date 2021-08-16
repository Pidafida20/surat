# Generated by Django 3.1.7 on 2021-08-06 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0042_auto_20210807_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surat',
            name='JENIS_SURAT',
            field=models.CharField(blank=True, choices=[('Surat Keterangan Usaha', 'Surat Keterangan Usaha'), ('Surat Keterangan Kehilangan', 'Surat Keterangan Kehilangan'), ('Surat Keterangan Domisii', 'Surat Keterangan Domisili'), ('Surat Keterangan Kematian', 'Surat Keterangan Kematian'), ('Surat Keterangan Tidak Mampu', 'Surat Keterangan Tidak Mampu'), ('Surat Keterangan Covid', 'Surat Keterangan Covid'), ('Surat Keterangan Kelakuan Baik', 'Surat Keterangan Kelakuan Baik'), ('Surat Keterangan Penghasilan', 'Surat Keterangan Penghasilan')], max_length=50, null=True),
        ),
    ]