# Generated by Django 3.1.7 on 2021-08-01 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0027_surat_no_telp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mayarakat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_surat', models.CharField(blank=True, max_length=50, null=True)),
                ('nik', models.CharField(blank=True, max_length=50, null=True)),
                ('nama_lengkap', models.CharField(blank=True, max_length=50, null=True)),
                ('jenis_usaha', models.CharField(blank=True, max_length=50, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=50, null=True)),
                ('no_telp', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Jenis_Surat',
            },
        ),
        migrations.RemoveField(
            model_name='surat',
            name='no_telp',
        ),
    ]
