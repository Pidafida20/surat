# Generated by Django 3.1.7 on 2021-05-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0003_penduduk_pendidikan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=200)),
                ('no_surat', models.CharField(max_length=200)),
                ('tanggal', models.CharField(max_length=200)),
                ('keterangan', models.CharField(max_length=200)),
                ('nik', models.CharField(max_length=200)),
                ('nama_lengkap', models.CharField(max_length=200)),
                ('jenis_kelamin', models.CharField(blank=True, choices=[('Laki-Laki', 'Laki-Laki'), ('Perempuan', 'Perempuan')], max_length=200, null=True)),
                ('tanggal_lahir', models.CharField(max_length=200)),
                ('pendidikan', models.CharField(blank=True, choices=[('SD', 'SD'), ('SLTP', 'SLTP'), ('SLTA', 'SLTA'), ('Pelajar/Mahasiswa', 'Pelajar/Mahasiswa')], max_length=200, null=True)),
                ('dusun', models.CharField(blank=True, choices=[('Dusun Matikan', 'Dusun Matikan'), ('Dusun Krajan', 'Dusun Krajan'), ('Dusun Kejawan', 'Dusun Kejawan')], max_length=200, null=True)),
                ('no_rt', models.CharField(max_length=200)),
                ('no_rw', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'sku',
            },
        ),
    ]