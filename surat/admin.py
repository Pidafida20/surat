from django.contrib import admin
from .models import  Surat, Jenis_Surat, Masyarakat, Penduduk, Petugas
from import_export .admin import ImportExportModelAdmin



admin.site.register(Surat)
admin.site.register(Jenis_Surat)
admin.site.register(Masyarakat)
admin.site.register(Petugas)
#Register your models here.
@admin.register(Penduduk)
class PendudukAdmin (ImportExportModelAdmin) :
    list_display = ("NO_KK", "NIK", "NAMA_LENGKAP", "STAT_HBKEL", "JENIS_KELAMIN", "TMPT_LAHIR", "TGL_LHR", "STATUS_KAWIN", "NAMA_IBU", "NAMA_AYAH", "AGAMA", "JENIS_PEKERJAAN", "ALAMAT", "NO_RT", "NO_RW", "NM_KEL", "NM_KEC", "KETERANGAN")
# @admin.register(Surat)
# class PendudukAdmin (ImportExportModelAdmin) :
#     list_display = '__all__' 
