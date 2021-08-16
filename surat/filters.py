import django_filters 
from .models import*
 
class PendudukFilter(django_filters.FilterSet):     
    class Meta:         
        model = Penduduk
        fields = ['NIK', 'NAMA_LENGKAP', 'ALAMAT']

class SuratFilter(django_filters.FilterSet):     
    class Meta:         
        model = Surat
        fields = ['JENIS_SURAT']

