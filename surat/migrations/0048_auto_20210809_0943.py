# Generated by Django 3.1.7 on 2021-08-09 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0047_auto_20210809_0457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surat',
            old_name='KEPERLUAN',
            new_name='CATATAN',
        ),
    ]