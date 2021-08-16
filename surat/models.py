from django.db import models
from datetime import datetime

from django.contrib.auth.models import User




# Create your models here.
class Petugas(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nama_petugas = models.CharField(max_length=50)
    nip_petugas = models.CharField(max_length=18)
    tempat_lahir_petugas = models.CharField(max_length=50)
    pendidikan_petugas = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    alamat = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=12)
    def __str__(self):
        return '%s' % (self.nama_petugas)
    class Meta:
        verbose_name_plural ="Petugas"

class Penduduk(models.Model):
    STAT_HBKEL = (
        ('KEPALA-KELUARGA', 'KEPALA-KELUARGA' ),
        ('ISTRI', 'ISTRI' ),
        ('ANAK', 'ANAK' ),
        ('CUCU', 'CUCU' ),
        ('FAMILI-LAIN', 'FAMILI-LAIN' ),
        ('MERTUA', 'MERTUA' ),
        ('ORANG-TUA', 'ORANG-TUA' ),
    )
    JENIS_KELAMIN = (
        ('LAKI-LAKI', 'LAKI-LAKI' ),
        ('PEREMPUAN', 'PEREMPUAN' ),
    )
    ALAMAT = (
        ('DUSUN KEJAWAN', 'DUSUN KEJAWAN' ),
        ('DUSUN MATIKAN', 'DUSUN MATIKAN' ),
        ('DUSUN KRAJAN', 'DUSUN KRAJAN' ),   
    )
    KETERANGAN = (
        ('MENINGGAL', 'MENINGGAL' ),
        ('PINDAH', 'PINDAH' ),
    )
    STATUS_KAWIN= (
        ('belum kawin', 'belum kawin' ),
        ('cerai hidup', 'cerai hidup' ),
        ('cerai mati', 'cerai mati' ),
        ('kawin', 'kawin' ),
        
    )
    TMPT_LAHIR =(
        ('BALI', 'BALI' ),
        ('BANYUWANGI', 'BANYUWANGI' ),
        ('BATANG', 'BATANG' ),
        ('BLITAR', 'BLITAR' ),
        ('BONDOWOSO', 'BONDOWOSO' ),
        ('BREBES', 'BREBES' ),
        ('CIREBON', 'CIREBON' ),
        ('DEWAN KALER', 'DEWAN KALER' ),
        ('DENPASAR', 'DENPASAR' ),
        ('GORONTALO', 'GORONTALO' ),
        ('GRESIK', 'GRESIK' ),
        ('JAKARTA', 'JAKARTA' ),
        ('JEMBER', 'JEMBER' ),
        ('JEPARA', 'JEPARA' ),
        ('JOMBANG', 'JOMBANG' ),
        ('KARANG ASEM', 'KARANG ASEM' ),
        ('KARAWANG', 'KARAWANG' ),
        ('KEBUMIN', 'KEBUMIN' ),
        ('KEDIRI', 'KEDIRI' ),
        ('KUTAI', 'KUTAI' ),
        ('LAMONGAN', 'LAMONGAN' ),
        ('LUMAJANG', 'LUMAJANG' ),
        ('MADIUN', 'MADIUN' ),
        ('MALANG', 'MALANG' ),
        ('MOJOKERTO', 'MOJOKERTO' ),
        ('NGANJUK', 'NGANJUK' ),
        ('NGAWI', 'NGAWI' ),
        ('PAMEKASAN', 'PAMEKASAN' ),
        ('PASER', 'PASER' ),
        ('PASURUAN', 'PASURUAN' ),
        ('PEMALANG', 'PEMLANG' ),
        ('PROBOLINGGO', 'PROBOLINGGO' ),
        ('SEMARANG', 'SEMARANG' ),
        ('SEMPULANG', 'SEMPULANG' ),
        ('SIDOARJO', 'SIDOARJO' ),
        ('SINGARAJA', 'SINGARAJA' ),
        ('SITUBONDO', 'SITUBONDO' ),
        ('SUBANG', 'SUBANG' ),
        ('SUKABUMI', 'SUKABUMI' ),
        ('SUMENEP', 'SUMENEP' ),
        ('SURABAYA', 'SURABAYA' ),
        ('TUBAN', 'TUBAN' ),
        ('TULUNG AGUNG', 'TULUNG AGUNG' ),

    )
    JENIS_PEKERJAAN = (
        ('APOTEKER', 'APOTEKER' ),
        ('BELUM/TIDAK BEKERJA', 'BELUM/TIDAK BEKERJA' ),
        ('BIDAN', 'BIDAN' ),
        ('BURUH HARIAN LEPAS', 'BURUH HARIAN LEPAS' ),
        ('BURUH PETERNAKAN', 'BURUH PETERNAKAN' ),
        ('BURUH TANI/PERKEBUNAN', 'BURUH TANI/PERKEBUNAN' ),
        ('DOSEN', 'DOSEN'),
        ('GURU', 'GURU' ),
        ('KARYAWAN BUMN', 'KARYAWAN BUMN' ),
        ('KARYAWAN HONORER', 'KARYAWAN HONORER' ),
        ('KARYAWAN SWASTA', 'KARYAWAN SWASTA' ),
        ('KEPOLISIAN RI', 'KEPOLISIAN RI' ),
        ('KONSTRUKSI', 'KONSTRUKSI' ),
        ('MEKANIK', 'MEKANIK' ),
        ('MENGURUS RUMAH TANGGA', 'MENGURUS RUMAH TANGGA' ),
        ('NELAYAN/PERIKANAN', 'NELAYAN/PERIKANAN' ),
        ('PEDAGANG', 'PEDAGANG' ),
        ('PEGAWAI NEGERI SIPIL', 'PEGAWAI NEGERI SIPIL' ),
        ('PELAJAR/MAHASISWA', 'PELAJAR/MAHASISWA' ),
        ('PEMBANTU RUMAH TANGGA', 'PEMBANTU RUMAH TANGGA' ),
        ('PENSIUNAN', 'PENSIUNAN' ),
        ('PERANGKAT DESA', 'PERANGKAT DESA' ),
        ('PERAWAT', 'PERAWAT' ),
        ('PERDAGANGAN', 'PERDAGANGAN' ),
        ('PETANI/PEKEBUN', 'PETANI/PEKEBUN' ),
        ('TRANSPORTASI', 'TRANSPORTASI' ),
        ('TUKANG BATU', 'TUKANG BATU' ),
        ('TUKANG JAHIT', 'TUKANG JAHIT' ),
        ('TUKANG KAYU', 'TUKANG KAYU' ),
        ('TUKANG LAS/PANDAI BESI', 'TUKANG LAS/PANDAI BESI' ),
        ('USTADZ/MUBALIGH', 'USTADZ/MUBALIGH' ),
        ('WIRASWASTA', 'WIRASWASTA' ),
    )
    
    NO_KK = models.CharField(max_length=16,blank=True, null=True)
    NIK = models.CharField(max_length=16,blank=True, null=True)
    NAMA_LENGKAP = models.CharField(max_length=100, blank=True, null=True)
    STAT_HBKEL = models.CharField(max_length=30, blank=True, null=True, choices=STAT_HBKEL)
    JENIS_KELAMIN = models.CharField(max_length=20, blank=True, null=True, choices=JENIS_KELAMIN)
    TMPT_LAHIR = models.CharField(max_length=25,  blank=True, null=True, choices=TMPT_LAHIR)
    TGL_LHR = models.CharField(max_length=25,blank=True, null=True,)
    STATUS_KAWIN = models.CharField(max_length=15, blank=True, null=True, choices=STATUS_KAWIN)
    NAMA_IBU = models.CharField(max_length=100, blank=True, null=True)
    NAMA_AYAH = models.CharField(max_length=100, blank=True, null=True)
    AGAMA = models.CharField(max_length=10, blank=True, null=True)
    JENIS_PEKERJAAN= models.CharField(max_length=100,blank=True, null=True, choices=JENIS_PEKERJAAN)
    ALAMAT = models.CharField(max_length=20,blank=True, null=True, choices=ALAMAT)
    NO_RT = models.CharField(max_length=3,blank=True, null=True)
    NO_RW = models.CharField(max_length=3,blank=True, null=True)
    NM_KEL = models.CharField(max_length=25,blank=True, null=True)
    NM_KEC = models.CharField(max_length=25, blank=True, null=True)
    KETERANGAN = models.CharField(max_length=50, blank=True, null=True, choices=KETERANGAN)
    
    def __str__(self):
        return '%s' % (self.NAMA_LENGKAP)
    class Meta:
        verbose_name_plural ="Penduduk"

class Surat(models.Model):
    STAT_HBKEL = (
        ('KEPALA-KELUARGA', 'KEPALA-KELUARGA' ),
        ('ISTRI', 'ISTRI' ),
        ('ANAK', 'ANAK' ),
        ('CUCU', 'CUCU' ),
        ('FAMILI-LAIN', 'FAMILI-LAIN' ),
        ('MERTUA', 'MERTUA' ),
        ('ORANG-TUA', 'ORANG-TUA' ),
    )
    JENIS_KELAMIN = (
        ('LAKI-LAKI', 'LAKI-LAKI' ),
        ('PEREMPUAN', 'PEREMPUAN' ),
    )
    ALAMAT = (
        ('DUSUN KEJAWAN', 'DUSUN KEJAWAN' ),
        ('DUSUN MATIKAN', 'DUSUN MATIKAN' ),
        ('DUSUN KRAJAN', 'DUSUN KRAJAN' ),   
    )
    KETERANGAN = (
        ('MENINGGAL', 'MENINGGAL' ),
        ('PINDAH', 'PINDAH' ),
    )
    STATUS_KAWIN= (
        ('belum kawin', 'belum kawin' ),
        ('cerai hidup', 'cerai hidup' ),
        ('cerai mati', 'cerai mati' ),
        ('kawin', 'kawin' ),
        
    )

    TMPT_LAHIR =(
        ('BALI', 'BALI' ),
        ('BANYUWANGI', 'BANYUWANGI' ),
        ('BATANG', 'BATANG' ),
        ('BLITAR', 'BLITAR' ),
        ('BONDOWOSO', 'BONDOWOSO' ),
        ('BREBES', 'BREBES' ),
        ('CIREBON', 'CIREBON' ),
        ('DEWAN KALER', 'DEWAN KALER' ),
        ('DENPASAR', 'DENPASAR' ),
        ('GORONTALO', 'GORONTALO' ),
        ('GRESIK', 'GRESIK' ),
        ('JAKARTA', 'JAKARTA' ),
        ('JEMBER', 'JEMBER' ),
        ('JEPARA', 'JEPARA' ),
        ('JOMBANG', 'JOMBANG' ),
        ('KARANG ASEM', 'KARANG ASEM' ),
        ('KARAWANG', 'KARAWANG' ),
        ('KEBUMIN', 'KEBUMIN' ),
        ('KEDIRI', 'KEDIRI' ),
        ('KUTAI', 'KUTAI' ),
        ('LAMONGAN', 'LAMONGAN' ),
        ('LUMAJANG', 'LUMAJANG' ),
        ('MADIUN', 'MADIUN' ),
        ('MALANG', 'MALANG' ),
        ('MOJOKERTO', 'MOJOKERTO' ),
        ('NGANJUK', 'NGANJUK' ),
        ('NGAWI', 'NGAWI' ),
        ('PAMEKASAN', 'PAMEKASAN' ),
        ('PASER', 'PASER' ),
        ('PASURUAN', 'PASURUAN' ),
        ('PEMALANG', 'PEMLANG' ),
        ('PROBOLINGGO', 'PROBOLINGGO' ),
        ('SEMARANG', 'SEMARANG' ),
        ('SEMPULANG', 'SEMPULANG' ),
        ('SIDOARJO', 'SIDOARJO' ),
        ('SINGARAJA', 'SINGARAJA' ),
        ('SITUBONDO', 'SITUBONDO' ),
        ('SUBANG', 'SUBANG' ),
        ('SUKABUMI', 'SUKABUMI' ),
        ('SUMENEP', 'SUMENEP' ),
        ('SURABAYA', 'SURABAYA' ),
        ('TUBAN', 'TUBAN' ),
        ('TULUNG AGUNG', 'TULUNG AGUNG' ),

    )
    JENIS_PEKERJAAN = (
        ('APOTEKER', 'APOTEKER' ),
        ('BELUM/TIDAK BEKERJA', 'BELUM/TIDAK BEKERJA' ),
        ('BIDAN', 'BIDAN' ),
        ('BURUH HARIAN LEPAS', 'BURUH HARIAN LEPAS' ),
        ('BURUH PETERNAKAN', 'BURUH PETERNAKAN' ),
        ('BURUH TANI/PERKEBUNAN', 'BURUH TANI/PERKEBUNAN' ),
        ('DOSEN', 'DOSEN'),
        ('GURU', 'GURU' ),
        ('KARYAWAN BUMN', 'KARYAWAN BUMN' ),
        ('KARYAWAN HONORER', 'KARYAWAN HONORER' ),
        ('KARYAWAN SWASTA', 'KARYAWAN SWASTA' ),
        ('KEPOLISIAN RI', 'KEPOLISIAN RI' ),
        ('KONSTRUKSI', 'KONSTRUKSI' ),
        ('MEKANIK', 'MEKANIK' ),
        ('MENGURUS RUMAH TANGGA', 'MENGURUS RUMAH TANGGA' ),
        ('NELAYAN/PERIKANAN', 'NELAYAN/PERIKANAN' ),
        ('PEDAGANG', 'PEDAGANG' ),
        ('PEGAWAI NEGERI SIPIL', 'PEGAWAI NEGERI SIPIL' ),
        ('PELAJAR/MAHASISWA', 'PELAJAR/MAHASISWA' ),
        ('PEMBANTU RUMAH TANGGA', 'PEMBANTU RUMAH TANGGA' ),
        ('PENSIUNAN', 'PENSIUNAN' ),
        ('PERANGKAT DESA', 'PERANGKAT DESA' ),
        ('PERAWAT', 'PERAWAT' ),
        ('PERDAGANGAN', 'PERDAGANGAN' ),
        ('PETANI/PEKEBUN', 'PETANI/PEKEBUN' ),
        ('TRANSPORTASI', 'TRANSPORTASI' ),
        ('TUKANG BATU', 'TUKANG BATU' ),
        ('TUKANG JAHIT', 'TUKANG JAHIT' ),
        ('TUKANG KAYU', 'TUKANG KAYU' ),
        ('TUKANG LAS/PANDAI BESI', 'TUKANG LAS/PANDAI BESI' ),
        ('USTADZ/MUBALIGH', 'USTADZ/MUBALIGH' ),
        ('WIRASWASTA', 'WIRASWASTA' ),
    )
    
    JENIS_SURAT = (
        ('Surat Keterangan Usaha', 'Surat Keterangan Usaha'),
        ('Surat Keterangan Tidak Mampu', 'Surat Keterangan Tidak Mampu'),
        ('Surat Keterangan Terdampak Covid', 'Surat Keterangan Terdampak Covid'),
        ('Surat Keterangan Penghasilan', 'Surat Keterangan Penghasilan'),
        ('Surat Keterangan Kematian', 'Surat Keterangan Kematian'),
        ('Surat Keterangan Kelakuan Baik', 'Surat Keterangan Kelakuan Baik'),
        ('Surat Keterangan Kehilangan', 'Surat Keterangan Kehilangan'),
        ('Surat Keterangan Domisili', 'Surat Keterangan Domisili'),
        
    )
    
    TANGGAL = models.CharField(max_length=20,blank=True, null=True)
    JENIS_SURAT = models.CharField(max_length=50, blank=True, null=True, choices=JENIS_SURAT)
    NO_SURAT = models.CharField(max_length=50, blank=True, null=True)
    NIK = models.CharField(max_length=16,blank=True, null=True)
    NAMA_LENGKAP = models.CharField(max_length=100, blank=True, null=True)
    STAT_HBKEL = models.CharField(max_length=30, blank=True, null=True, choices=STAT_HBKEL)
    JENIS_KELAMIN = models.CharField(max_length=20, blank=True, null=True, choices=JENIS_KELAMIN)
    TMPT_LAHIR = models.CharField(max_length=25,  blank=True, null=True, choices=TMPT_LAHIR)
    TGL_LHR = models.CharField(max_length=25,blank=True, null=True,)
    STATUS_KAWIN = models.CharField(max_length=15, blank=True, null=True, choices=STATUS_KAWIN)
    NAMA_IBU = models.CharField(max_length=100, blank=True, null=True)
    NAMA_AYAH = models.CharField(max_length=100, blank=True, null=True)
    AGAMA = models.CharField(max_length=10, blank=True, null=True)
    JENIS_PEKERJAAN = models.CharField(max_length=100,blank=True, null=True, choices=JENIS_PEKERJAAN)
    ALAMAT = models.CharField(max_length=50,blank=True, null=True, choices=ALAMAT)
    NO_RT = models.CharField(max_length=3,blank=True, null=True)
    NO_RW = models.CharField(max_length=3,blank=True, null=True)
    NM_KEL = models.CharField(max_length=20,blank=True, null=True)
    NM_KEC = models.CharField(max_length=20, blank=True, null=True)
    KETERANGAN = models.CharField(max_length=100, blank=True, null=True)
    CATATAN = models.CharField(max_length=250, blank=True, null=True)
    BULAN = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.NAMA_LENGKAP)
    class Meta:
        verbose_name_plural ="Surat"

class Jenis_Surat(models.Model):

    
    JENIS_SURAT = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.JENIS_SURAT)
    class Meta:
        verbose_name_plural ="Jenis_Surat"

class Masyarakat(models.Model):

    jenis_surat = models.CharField(max_length=50, blank=True, null=True)
    nik = models.CharField(max_length=50, blank=True, null=True)
    nama_lengkap = models.CharField(max_length=50, blank=True, null=True)
    catatan = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)
    no_telp = models.CharField(max_length=12, blank=True, null=True)
    def __str__(self):
        return '%s' % (self.nik)
    class Meta:
        verbose_name_plural ="Masyarakat"




