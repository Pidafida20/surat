# Generated by Django 3.1.7 on 2021-08-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surat', '0038_auto_20210806_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jenis_surat',
            old_name='jenis_surat',
            new_name='JENIS_SURAT',
        ),
        migrations.RenameField(
            model_name='penduduk',
            old_name='nama_lengkap',
            new_name='NAMA_AYAH',
        ),
        migrations.RenameField(
            model_name='surat',
            old_name='bulan',
            new_name='BULAN',
        ),
        migrations.RenameField(
            model_name='surat',
            old_name='jenis_usaha',
            new_name='JENIS_USAHA',
        ),
        migrations.RenameField(
            model_name='surat',
            old_name='keterangan',
            new_name='NAMA_AYAH',
        ),
        migrations.RenameField(
            model_name='surat',
            old_name='nama_lengkap',
            new_name='NAMA_IBU',
        ),
        migrations.RenameField(
            model_name='surat',
            old_name='no_surat',
            new_name='NO_SURAT',
        ),
        migrations.RemoveField(
            model_name='jenis_surat',
            name='no_surat',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='desa',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='dusun',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='jenis_kelamin',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='keterangan',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='kode_pos',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='nik',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='no_kk',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='no_rt',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='no_rw',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='pendidikan',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='stat_hbkel',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='status_perkawinan',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='tanggal_lahir',
        ),
        migrations.RemoveField(
            model_name='penduduk',
            name='tempat_lahir',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='desa',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='dusun',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='jenis_kelamin',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='jenis_surat',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='nik',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='no_rt',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='no_rw',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='pendidikan',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='status_perkawinan',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='tanggal_lahir',
        ),
        migrations.RemoveField(
            model_name='surat',
            name='tempat_lahir',
        ),
        migrations.AddField(
            model_name='penduduk',
            name='AGAMA',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='ALAMAT',
            field=models.CharField(blank=True, choices=[('DUSUN KEJAWAN', 'DUSUN KEJAWAN'), ('DUSUN MATIKAN', 'DUSUN MATIKAN'), ('DUSUN KRAJAN', 'DUSUN KRAJAN')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='JENIS_KELAMIN',
            field=models.CharField(blank=True, choices=[('LAKI-LAKI', 'LAKI-LAKI'), ('PEREMPUAN', 'PEREMPUAN')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='JENIS_PEKERJAAN',
            field=models.CharField(blank=True, choices=[('APOTEKER', 'APOTEKER'), ('BEELUM/TIDAK BEKERJA', 'BEELUM/TIDAK BEKERJA'), ('BIDAN', 'SLTA'), ('BURUH HARIAN LEPAS', 'BURUH HARIAN LEPAS'), ('BURUH PETERNAKAN', 'BURUH PETERNAKAN'), ('BURUH TANI/PERKEBUNAN', 'BURUH TANI/PERKEBUNAN'), ('GURU', 'GURU'), ('KARYAWAN BUMN', 'KARYAWAN BUMN'), ('KARYAWAN HONORER', 'KARYAWAN HONORER'), ('KARYAWAN SWASTA', 'KARYAWAN SWASTA'), ('KEPOLISIAN RI', 'KEPOLISIAN RI'), ('MENGURUS RUMAH TANGGA', 'MENGURUS RUMAH TANGGA'), ('NELAYAN/PERIKANAN', 'NELAYAN/PERIKANAN'), ('PEDAGANG', 'PEDAGANG'), ('PEGAWAI NEGERI SIPIL', 'PEGAWAI NEGERI SIPIL'), ('PELAJAR/MAHAISWA', 'PELAJAR/MAHAISWA'), ('PEMBANTU RUMAH TANGGA', 'PEMBANTU RUMAH TANGGA'), ('PENSIUNAN', 'PENSIUNAN'), ('PERANGKAT DESA', 'PERANGKAT DESA'), ('PERAWAT', 'PERAWAT'), ('PERDAGANGAN', 'PERDAGANGAN'), ('PETANI/PEKEBUN', 'PETANI/PEKEBUN'), ('TUKANG JAHIT', 'TUKANG JAHIT'), ('WIRASWASTA', 'WIRASWASTA')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='KETERANGAN',
            field=models.CharField(blank=True, choices=[('MENINGGAL', 'MENINGGAL'), ('PINDAH', 'PINDAH')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NAMA_IBU',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NAMA_LENGKAP',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NIK',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NM_KEC',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NM_KEL',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NO_KK',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NO_RT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='NO_RW',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='STATUS_KAWIN',
            field=models.CharField(blank=True, choices=[('belum kawin', 'belum kawin'), ('cerai hidup', 'cerai hidup'), ('cerai mati', 'cerai mati'), ('kawin', 'kawin')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='STAT_HBKEL',
            field=models.CharField(blank=True, choices=[('KEPALA-KELUARGA', 'KEPALA-KELUARGA'), ('ISTRI', 'ISTRI'), ('ANAK', 'ANAK'), ('CUCU', 'CUCU'), ('FAMILI-LAIN', 'FAMILI-LAIN'), ('MERTUA', 'MERTUA'), ('ORANG-TUA', 'ORANG-TUA')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='TGL_LHR',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='penduduk',
            name='TMPT_LAHIR',
            field=models.CharField(blank=True, choices=[('BALI', 'BALI'), ('BANYUWANGI', 'BANYUWANGI'), ('BATANG', 'BATANG'), ('BLITAR', 'BLITAR'), ('BONDOWOSO', 'BONDOWOSO'), ('BREBES', 'BREBES'), ('CIREBON', 'CIREBON'), ('DEWAN KALER', 'DEWAN KALER'), ('DENPASAR', 'DENPASAR'), ('GORONTALO', 'GORONTALO'), ('GRESIK', 'GRESIK'), ('JAKARTA', 'JAKARTA'), ('JEMBER', 'JEMBER'), ('JEPARA', 'JEPARA'), ('JOMBANG', 'JOMBANG'), ('KARANG ASEM', 'KARANG ASEM'), ('KARAWANG', 'KARAWANG'), ('KEBUMIN', 'KEBUMIN'), ('KEDIRI', 'KEDIRI'), ('KUTAI', 'KUTAI'), ('LAMONGAN', 'LAMONGAN'), ('LUMAJANG', 'LUMAJANG'), ('MADIUN', 'MADIUN'), ('MALANG', 'MALANG'), ('MOJOKERTO', 'MOJOKERTO'), ('NGANJUK', 'NGANJUK'), ('NGAWI', 'NGAWI'), ('PAMEKASAN', 'PAMEKASAN'), ('PASER', 'PASER'), ('PASURUAN', 'PASURUAN'), ('PEMALANG', 'PEMLANG'), ('PROBOLINGGO', 'PROBOLINGGO'), ('SEMARANG', 'SEMARANG'), ('SEMPULANG', 'SEMPULANG'), ('SIDOARJO', 'SIDOARJO'), ('SINGARAJA', 'SINGARAJA'), ('SITUBONDO', 'SITUBONDO'), ('SUBANG', 'SUBANG'), ('SUKABUMI', 'SUKABUMI'), ('SUMENEP', 'SUMENEP'), ('SURABAYA', 'SURABAYA'), ('TUBAN', 'TUBAN'), ('TULUNG AGUNG', 'TULUNG AGUNG')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='AGAMA',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='ALAMAT',
            field=models.CharField(blank=True, choices=[('DUSUN KEJAWAN', 'DUSUN KEJAWAN'), ('DUSUN MATIKAN', 'DUSUN MATIKAN'), ('DUSUN KRAJAN', 'DUSUN KRAJAN')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='JENIS_KELAMIN',
            field=models.CharField(blank=True, choices=[('LAKI-LAKI', 'LAKI-LAKI'), ('PEREMPUAN', 'PEREMPUAN')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='JENIS_PEKERJAAN',
            field=models.CharField(blank=True, choices=[('APOTEKER', 'APOTEKER'), ('BEELUM/TIDAK BEKERJA', 'BEELUM/TIDAK BEKERJA'), ('BIDAN', 'SLTA'), ('BURUH HARIAN LEPAS', 'BURUH HARIAN LEPAS'), ('BURUH PETERNAKAN', 'BURUH PETERNAKAN'), ('BURUH TANI/PERKEBUNAN', 'BURUH TANI/PERKEBUNAN'), ('GURU', 'GURU'), ('KARYAWAN BUMN', 'KARYAWAN BUMN'), ('KARYAWAN HONORER', 'KARYAWAN HONORER'), ('KARYAWAN SWASTA', 'KARYAWAN SWASTA'), ('KEPOLISIAN RI', 'KEPOLISIAN RI'), ('MENGURUS RUMAH TANGGA', 'MENGURUS RUMAH TANGGA'), ('NELAYAN/PERIKANAN', 'NELAYAN/PERIKANAN'), ('PEDAGANG', 'PEDAGANG'), ('PEGAWAI NEGERI SIPIL', 'PEGAWAI NEGERI SIPIL'), ('PELAJAR/MAHAISWA', 'PELAJAR/MAHAISWA'), ('PEMBANTU RUMAH TANGGA', 'PEMBANTU RUMAH TANGGA'), ('PENSIUNAN', 'PENSIUNAN'), ('PERANGKAT DESA', 'PERANGKAT DESA'), ('PERAWAT', 'PERAWAT'), ('PERDAGANGAN', 'PERDAGANGAN'), ('PETANI/PEKEBUN', 'PETANI/PEKEBUN'), ('TUKANG JAHIT', 'TUKANG JAHIT'), ('WIRASWASTA', 'WIRASWASTA')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='JENIS_SURAT',
            field=models.CharField(blank=True, choices=[('Surat Keterangan Usaha', 'Surat Keterangan Usaha'), ('Surat Keterangan KTP', 'Surat Keterangan KTP'), ('Surat Keterangan Kematian', 'Surat Keterangan Kematian'), ('Surat Keterangan Kelahiran', 'Surat Keterangan Kelahiran'), ('Surat Keterangan Catatan Kepolian ', 'Surat Keterangan Catatan Kepolisian'), ('Surat Keterangan penduduk tetap', 'Surat Keterangan penduduk tetap'), ('Surat Keterangan Pindah', 'Surat Keterangan Pindah'), ('Surat Keterangan KTP', 'Surat Keterangan KTP')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='KETERANGAN',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='NAMA_LENGKAP',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='NIK',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='NM_KEC',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='NM_KEL',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='NO_KK',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='NO_RT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='NO_RW',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='STATUS_KAWIN',
            field=models.CharField(blank=True, choices=[('belum kawin', 'belum kawin'), ('cerai hidup', 'cerai hidup'), ('cerai mati', 'cerai mati'), ('kawin', 'kawin')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='STAT_HBKEL',
            field=models.CharField(blank=True, choices=[('KEPALA-KELUARGA', 'KEPALA-KELUARGA'), ('ISTRI', 'ISTRI'), ('ANAK', 'ANAK'), ('CUCU', 'CUCU'), ('FAMILI-LAIN', 'FAMILI-LAIN'), ('MERTUA', 'MERTUA'), ('ORANG-TUA', 'ORANG-TUA')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='TGL_LHR',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='surat',
            name='TMPT_LAHIR',
            field=models.CharField(blank=True, choices=[('BALI', 'BALI'), ('BANYUWANGI', 'BANYUWANGI'), ('BATANG', 'BATANG'), ('BLITAR', 'BLITAR'), ('BONDOWOSO', 'BONDOWOSO'), ('BREBES', 'BREBES'), ('CIREBON', 'CIREBON'), ('DEWAN KALER', 'DEWAN KALER'), ('DENPASAR', 'DENPASAR'), ('GORONTALO', 'GORONTALO'), ('GRESIK', 'GRESIK'), ('JAKARTA', 'JAKARTA'), ('JEMBER', 'JEMBER'), ('JEPARA', 'JEPARA'), ('JOMBANG', 'JOMBANG'), ('KARANG ASEM', 'KARANG ASEM'), ('KARAWANG', 'KARAWANG'), ('KEBUMIN', 'KEBUMIN'), ('KEDIRI', 'KEDIRI'), ('KUTAI', 'KUTAI'), ('LAMONGAN', 'LAMONGAN'), ('LUMAJANG', 'LUMAJANG'), ('MADIUN', 'MADIUN'), ('MALANG', 'MALANG'), ('MOJOKERTO', 'MOJOKERTO'), ('NGANJUK', 'NGANJUK'), ('NGAWI', 'NGAWI'), ('PAMEKASAN', 'PAMEKASAN'), ('PASER', 'PASER'), ('PASURUAN', 'PASURUAN'), ('PEMALANG', 'PEMLANG'), ('PROBOLINGGO', 'PROBOLINGGO'), ('SEMARANG', 'SEMARANG'), ('SEMPULANG', 'SEMPULANG'), ('SIDOARJO', 'SIDOARJO'), ('SINGARAJA', 'SINGARAJA'), ('SITUBONDO', 'SITUBONDO'), ('SUBANG', 'SUBANG'), ('SUKABUMI', 'SUKABUMI'), ('SUMENEP', 'SUMENEP'), ('SURABAYA', 'SURABAYA'), ('TUBAN', 'TUBAN'), ('TULUNG AGUNG', 'TULUNG AGUNG')], max_length=25, null=True),
        ),
    ]
