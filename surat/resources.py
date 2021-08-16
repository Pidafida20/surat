from import_export import resources
from .models import Penduduk, Surat

class PendudukResource (resources.ModelResource):
    class Meta:
        model = Penduduk

class SuratResource (resources.ModelResource):
    class Meta:
        model = Surat