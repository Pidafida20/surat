from django import forms
from django.forms import ModelForm
from .models import *

class DataForm(ModelForm):
    class Meta:
        model = Penduduk
        fields = '__all__'

        widgets = {
            'NO_KK' : forms.TextInput(attrs={'class' : 'form-control' }),
            'NIK' : forms.TextInput(attrs={'class': 'form-control'}),
            'NAMA_LENGKAP' : forms.TextInput(attrs={'class': 'form-control'}),
            'STAT_HBKEL': forms.Select(attrs={'class': 'form-control'}),
            'JENIS_KELAMIN': forms.Select(attrs={'class': 'form-control'}),
            'TMPT_LAHIR' : forms.Select(attrs={'class': 'form-control'}),
            'TGL_LHR' : forms.TextInput(attrs={'class': 'form-control'}),
            'STATUS_KAWIN': forms.Select(attrs={'class': 'form-control'}),
            'NAMA_IBU': forms.TextInput(attrs={'class': 'form-control'}),
            'NAMA_AYAH': forms.TextInput(attrs={'class': 'form-control'}),
            'AGAMA': forms.TextInput(attrs={'class': 'form-control'}),
            'JENIS_PEKERJAAN' : forms.Select(attrs={'class': 'form-control'}),
            'ALAMAT' : forms.Select(attrs={'class': 'form-control'}),
            'NO_RT' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number' }),
            'NO_RW' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number' }),
            'NM_KEL' : forms.TextInput(attrs={'class': 'form-control'}),
            'NM_KEC' : forms.TextInput(attrs={'class': 'form-control'}),
            'KETERANGAN' : forms.Select(attrs={'class': 'form-control'}),
        }
        labels ={
            'NO_KK': 'NO KK',
            'NIK': 'NIK',
            'NAMA_LENGKAP':'NAMA LENGKAP',
            'STAT_HBKEL': 'STATUS HUBKEL',
            'JENIS_KELAMIN': 'JENIS KELAMIN',
            'TMPT_LAHIR': 'TEMPAT LAHIR',
            'TGL_LHR': 'TANGGAL LAHIR' ,
            'STATUS_KAWIN': 'STATUS KAWIN',
            'NAMA_IBU': 'NAMA BU',
            'NAMA_AYAH': 'NAMA AYAH',
            'AGAMA': 'AGAMA',
            'JENIS_PEKERJAAN':'JENIS PEKERJAAN',
            'ALAMAT':'ALAMAT',
            'NO_RT':'NO RT',
            'NO_RW':'NO RW',
            'NM_KEL':'NM KEL',
            'NM_KEC':'NM KEC',
            'KETERANGAN':'KETERANGAN',
            

        }
class SuratForm(ModelForm):
    class Meta:
        model = Surat
        fields = '__all__'

        widgets = {
            'TANGGAL': forms.TextInput(attrs={'class': 'form-control'}),
            'JENIS_SURAT': forms.Select(attrs={'class': 'form-control'}),
            'NO_SURAT' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number' }),
            'NIK' : forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
            'NAMA_LENGKAP' : forms.TextInput(attrs={'class': 'form-control'}),
            'STAT_HBKEL': forms.Select(attrs={'class': 'form-control'}),
            'JENIS_KELAMIN': forms.Select(attrs={'class': 'form-control'}),
            'TMPT_LAHIR' : forms.Select(attrs={'class': 'form-control'}),
            'TGL_LHR' : forms.TextInput(attrs={'class': 'form-control'}),
            'STATUS_KAWIN': forms.Select(attrs={'class': 'form-control'}),
            'NAMA_IBU': forms.TextInput(attrs={'class': 'form-control'}),
            'NAMA_AYAH': forms.TextInput(attrs={'class': 'form-control'}),
            'AGAMA': forms.TextInput(attrs={'class': 'form-control'}),
            'JENIS_PEKERJAAN' : forms.Select(attrs={'class': 'form-control'}),
            'ALAMAT' : forms.Select(attrs={'class': 'form-control'}),
            'NO_RT' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number' }),
            'NO_RW' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number' }),
            'NM_KEL' : forms.TextInput(attrs={'class': 'form-control'}),
            'NM_KEC' : forms.TextInput(attrs={'class': 'form-control'}),
            'KETERANGAN' : forms.TextInput(attrs={'class': 'form-control'}),
            'CATATAN' : forms.TextInput(attrs={'class': 'form-control'}),
            'BULAN' : forms.TextInput(attrs={'class' : 'form-control' }),

        }
        labels ={
            'TANGGAL' : 'TANGGAL',
            'JENIS_SURAT' : 'JENIS SURAT',
            'NO_SURAT': 'NO SURAT',
            'NO_KK': 'NO KK',
            'NIK': 'NIK',
            'NAMA_LENGKAP':'NAMA LENGKAP',
            'STAT_HBKEL': 'STATUS HUBKEL',
            'JENIS_KELAMIN': 'JENIS KELAMIN',
            'TMPT_LAHIR': 'TEMPAT LAHIR',
            'TGL_LHR': 'TANGGAL LAHIR' ,
            'STATUS_KAWIN': 'STATUS KAWIN',
            'NAMA_IBU': 'NAMA BU',
            'NAMA_AYAH': 'NAMA AYAH',
            'AGAMA': 'AGAMA',
            'JENIS_PEKERJAAN':'JENIS PEKERJAAN',
            'ALAMAT':'ALAMAT',
            'NO_RT':'NO RT',
            'NO_RW':'NO RW',
            'NM_KEL':'NM KEL',
            'NM_KEC':'NM KEC',
            'KETERANGAN':'KETERANGAN',
            'CATATAN':'CATATAN',
            'BULAN' : 'BULAN',
 
        }

class JenisSuratForm(ModelForm):
    class Meta:
        model = Jenis_Surat
        fields = ['JENIS_SURAT']

        widgets = {
            
            'JENIS_SURAT': forms.TextInput(attrs={'class': 'form-control'}),
            # 'keterangan_jenis': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels ={
            'JENIS_SURAT' : 'JENIS_SURAT',
            # 'keterangan_jenis' : 'Keterangan Jenis',
        }    

            
class PetugasForm(ModelForm):
    class Meta:
        model = Petugas
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'nama_petugas': forms.TextInput(attrs={'class': 'form-control'}),
            'nip_petugas' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number' }),
            'tempat_lahir_petugas' : forms.TextInput(attrs={'class': 'form-control'}),
            'pendidikan_petugas' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control','type':'email'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'no_hp' : forms.TextInput(attrs={'class' : 'form-control' }),
           

        }
        labels ={
            'nama_petugas' : 'Nama Lengkap',
            'nip_petugas': 'NIP ',
            'tempat_lahir_petugas': 'Tempat, Tanggal Lahir ',
            'pendidikan_petugas' : 'Pendidikan',
            'email': 'Email',
            'alamat': 'Alamat',
            'no_hp' : 'No HP ',
           
        }   

class MasyarakatForm(ModelForm):
    class Meta:
        model = Masyarakat
        fields = '__all__'
        # exclude = ['user']

        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nik' : forms.TextInput(attrs={'class' : 'form-control', 'type':'number' }),
            'jenis_surat' : forms.Select(attrs={'class': 'form-control'}),
            'no_hp' : forms.TextInput(attrs={'class': 'form-control'}),
            'keperluan' : forms.TextInput(attrs={'class': 'form-control','type':'email'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels ={
            'nama_lengap' : 'Nama Lengkap',
            'nik': 'NIK ',
            'jenis_surat': 'Jenis Surat',
            'no_hp' : 'No Telepon',
            'keperluan': 'Keperluan',
            'keterangan': 'Keterangan',
        } 


        
