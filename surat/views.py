from django.shortcuts import render, redirect,get_object_or_404
from django.http import  HttpResponse
from surat.resources import PendudukResource, SuratResource
from django.core.paginator import Paginator 
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from tablib import Dataset
from .forms import *
from .models import *
from xhtml2pdf import pisa
from django.template.loader import get_template
from .filters import *

import json

from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login

# Create your views here.

@login_required(login_url='login')
@pilihan_login
def beranda(request):
    datapenduduk = Penduduk.objects.all()
    list_surat = Surat.objects.all()
    total_penduduk = Penduduk.objects.count()
    total_kematian = datapenduduk.filter(KETERANGAN = 'MENINGGAL'). count()
    total_pindah= datapenduduk.filter(KETERANGAN = 'PINDAH'). count()
    total_surat = Surat.objects.count()
    total_mati= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kematian'). count()
    total_domisili= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Domisili'). count()
    total_covid = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Terdampak Covid'). count()
    total_usaha= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Usaha'). count()
    total_skkb = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kelakuan Baik'). count()
    total_sktm = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Tidak Mampu'). count()
    total_hilang = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kehilangan'). count()
    total_hasil = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Penghasilan'). count()
    context = {
        "menu" : 'Beranda',
        "page" : 'Selamat Datang di Aplikasi Layanan Surat',
        'dt_penduduk' : datapenduduk,
        'data_penduduk' : total_penduduk,
        'data_kematian' : total_kematian,
        'data_pendudukpindah' : total_pindah,

        'jumlah_surat' : total_surat,
        'surat_kematian' : total_mati,
        'surat_covid' : total_covid,
        'surat_domisili' : total_domisili,
        'surat_usaha' : total_usaha,
        'surat_skkb' : total_skkb,
        'surat_sktm' : total_sktm,
        'surat_hilang' : total_hilang,
        'surat_hasil' : total_hasil,

    }
    return render(request, 'surat/beranda.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def penduduk(request):
    list_penduduk = Penduduk.objects.order_by('-NO_KK')
    filter_penduduk = PendudukFilter(request.GET, queryset=list_penduduk)     
    list_penduduk=filter_penduduk.qs
    halaman_tampil = Paginator(list_penduduk, 100)     
    halaman_url = request.GET.get('halaman',1)     
    halaman_penduduk = halaman_tampil.get_page(halaman_url)

    if halaman_penduduk.has_previous(): 
        url_previous = f'?halaman={halaman_penduduk.previous_page_number()}'    
    else:         
        url_previous = '' 
    if halaman_penduduk.has_next():         
        url_next = f'?halaman={halaman_penduduk.next_page_number()}'     
    else:         
        url_next = ''
    context = {
        "menu" : 'Data ',
        "page" : 'Data Penduduk',
        "tampil" : list_penduduk,         
        'halaman_list_penduduk':halaman_penduduk,
        'filter_list_penduduk': filter_penduduk,
        'previous' : url_previous,         
        'next' : url_next,
        
    }
    return render(request, 'surat/penduduk.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def tambahpenduduk(request):
    tambahpenduduk = DataForm()
    if request.method == 'POST' :
        #print('cetak POST:', request.POST)
        formsimpan = DataForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('penduduk')
    context = {
        "menu" : 'tambah penduduk',
        "page" : 'tambah-Penduduk',
        "tambahpenduduk": tambahpenduduk,
    }
    return render(request, 'surat/tambahpenduduk.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def editpenduduk (request, pk):
    up_penduduk = Penduduk.objects.get(id=pk)
    editpenduduk = DataForm(instance=up_penduduk)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = DataForm(request.POST, instance=up_penduduk)
        if formedit.is_valid:
            formedit.save()
            return redirect('penduduk')
    context = {
        "menu" : 'editpenduduk',
        "page" : 'Edit Penduduk',
        "editpenduduk" : editpenduduk,
    }
    return render(request, 'surat/editpenduduk.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def jenissurat(request):
    list_jenissurat = Jenis_Surat.objects.order_by('-JENIS_SURAT')
    context = {
        "menu" : 'Jenis',
        "page" : 'Jenis Surat',
        "tampil" : list_jenissurat,
    }
    return render(request, 'surat/jenissurat.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def tambahjenissurat(request):
    tambahjenissurat = JenisSuratForm()
    if request.method == 'POST' :
        #print('cetak POST:', request.POST)
        formsimpan = JenisSuratForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('jenissurat')
    context = {
        "menu" : 'tambah jenis surat',
        "page" : 'tambah-jenis-surat',
        "tampil": tambahjenissurat,
    }
    return render(request, 'surat/tambahjenissurat.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def layanansurat (request):
    no = Surat.objects.all().count()

    nosurat = 1 + int(no)
    context = {
        "menu" : 'halaman input surat',
        "page" : 'tambah surat',
        'nosurat' : nosurat
    }
    return render(request, 'surat/inputsurat.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def inputsurat(request):
    if request.method == 'POST':
        NO_SURAT = request.POST.get('NO_SURAT')
        JENIS_SURAT = request.POST.get('JENIS_SURAT')
        TANGGAL= request.POST.get('TANGGAL')
        NIK = request.POST.get('NIK')
        NAMA_LENGKAP = request.POST.get('NAMA_LENGKAP')
        STAT_HBKEL = request.POST.get('STAT_HBKEL')
        JENIS_KELAMIN = request.POST.get('JENIS_KELAMIN')
        TMPT_LAHIR = request.POST.get('TMPT_LAHIR')
        TGL_LHR = request.POST.get('TGL_LHR')
        STATUS_KAWIN = request.POST.get('STATUS_KAWIN')
        NAMA_IBU = request.POST.get('NAMA_IBU')
        NAMA_AYAH = request.POST.get('NAMA_AYAH')
        AGAMA = request.POST.get('AGAMA')
        JENIS_PEKERJAAN = request.POST.get('JENIS_PEKERJAAN')
        ALAMAT = request.POST.get('ALAMAT')
        NO_RT = request.POST.get('NO_RT')
        NO_RW = request.POST.get('NO_RW')
        NM_KEL = request.POST.get('NM_KEL')
        NM_KEC = request.POST.get('NM_KEC')
        KETERANGAN = request.POST.get('KETERANGAN')
        CATATAN = request.POST.get('CATATAN')
        BULAN = request.POST.get('BULAN')

        simpan = Surat.objects.create(NO_SURAT=NO_SURAT,JENIS_SURAT=JENIS_SURAT,TANGGAL=TANGGAL, NIK=NIK, NAMA_LENGKAP=NAMA_LENGKAP, STAT_HBKEL=STAT_HBKEL, JENIS_KELAMIN=JENIS_KELAMIN, TMPT_LAHIR=TMPT_LAHIR, TGL_LHR=TGL_LHR, STATUS_KAWIN=STATUS_KAWIN, NAMA_IBU=NAMA_IBU, NAMA_AYAH=NAMA_AYAH, AGAMA=AGAMA, JENIS_PEKERJAAN=JENIS_PEKERJAAN, ALAMAT=ALAMAT, NO_RT=NO_RT, NO_RW=NO_RW, NM_KEL=NM_KEL, NM_KEC=NM_KEC, KETERANGAN=KETERANGAN, CATATAN=CATATAN, BULAN=BULAN )
        simpan.save()

    return JsonResponse({'status' : 0})

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def surat(request):
    list_surat = Surat.objects.order_by('-TANGGAL')
    filter_surat = SuratFilter(request.GET, queryset=list_surat)     
    list_surat = filter_surat.qs
    halaman_tampil = Paginator(list_surat, 20)     
    halaman_url = request.GET.get('halaman',1)     
    halaman_surat = halaman_tampil.get_page(halaman_url)

    if halaman_surat.has_previous(): 
        url_previous = f'?halaman={halaman_surat.previous_page_number()}'    
    else:         
        url_previous = '' 
    if halaman_surat.has_next():         
        url_next = f'?halaman={halaman_surat.next_page_number()}'     
    else:         
        url_next = ''
    context = {
        "menu" : 'Data ',
        "page" : 'Data Surat',
        "list" : list_surat,
        'halaman_list_surat':halaman_surat,
        'filter_list_surat': filter_surat,
        'previous' : url_previous,         
        'next' : url_next,
    }
    return render(request, 'surat/surat.html', context)

def hapussurat(request, pk):
    hapussurat = Surat.objects.get(id=pk)
    if request.method == 'POST':
        hapussurat.delete()
        return redirect('surat')
    context = {
        "menu" : 'hapussurat',
        "page" : 'Hapus Surat',
        "hapussurat" : hapussurat,
    }
    return render(request, 'surat/hapussurat.html', context)


def editsurat (request, pk):
    ed_surat = Surat.objects.get(id=pk)
    editsurat = SuratForm(instance=ed_surat)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = SuratForm(request.POST, instance=ed_surat)
        if formedit.is_valid:
            formedit.save()
            return redirect('surat')
    context = {
        "menu" : 'edit surat',
        "page" : 'Edit Surat',
        "editsurat" : editsurat,
    }
    return render(request, 'surat/editsurat.html', context)

# def jenissurat(request):
#     context = {
#         "menu" : 'surat ',
#         "page" : 'jenis surat'
#     }
#     return render(request, 'surat/jenissurat.html', context)

@tolakhalaman_ini
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        cocok = authenticate(request, username=username, password=password)
        if cocok is not None:
            login(request, cocok)
            return redirect('beranda')
        else:
            messages.error(request, "Username / Password Tidak Cocok")
            return redirect('login')

    context = {
        "menu" : 'Halaman Login',
        "page" : 'login',
    }
    return render(request, 'surat/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')



def export (request):
    penduduk_resource = PendudukResource()
    dataset = penduduk_resource.export()
    response = HttpResponse(dataset.xls, content_type = 'application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data Penduduk.xls"'

    return response

def upload(request) :
    if request.method == 'POST' :
        penduduk_resource = PendudukResource()
        dataset = Dataset()
        new_penduduk = request.FILES['myfile']

        if not new_penduduk.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_penduduk.read(), format='xlsx')
        for data in imported_data:
            value = Penduduk(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
                data[13],
                data[14],
                data[15],
                data[16],
                data[17],
                data[18]

                )
            value.save()
    return render(request, 'upload.html')




def ambilnik(request):
    if request.method == "POST":
        NIK = request.POST.get('NIK')
        # if Penduduk.objects.filter(username = username).first():

        if Penduduk.objects.filter(NIK=NIK).first():
            nilai = get_object_or_404(Penduduk, NIK=NIK)
            # nama = nilai.nama_lengkap
            # tempat = nilai.tempat_lahir
            response = {
                'nama':nilai.NAMA_LENGKAP, 
                'stat_hbkel':nilai.STAT_HBKEL,
                'jk':nilai.JENIS_KELAMIN,
                'tempat_lahir':nilai.TMPT_LAHIR, 
                'tgllhr':nilai.TGL_LHR,
                'status_kawin':nilai.STATUS_KAWIN,
                'ibu':nilai.NAMA_IBU, 
                'ayah':nilai.NAMA_AYAH,
                'agama':nilai.AGAMA,
                'jenis_pekerjaan':nilai.JENIS_PEKERJAAN,
                'alamat':nilai.ALAMAT, 
                'rt':nilai.NO_RT,
                'rw':nilai.NO_RW,
                'kel':nilai.NM_KEL, 
                'kec':nilai.NM_KEC,
                

            }
            
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse({'status' : 0})
                
#pdf surat

def pdf_usaha(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_usaha.html', context)

def pdf_covid(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_covid.html', context)
    

def pdf_tidakmampu(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_tidakmampu.html', context)
   

def pdf_kelakuanbaik(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_kelakuanbaik.html', context)
    

def pdf_kehilangan(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_kehilangan.html', context)
    
def pdf_domisili(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_domisili.html', context)

    
def pdf_kematian(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    
    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_kematian.html', context)
    


def pdf_penghasilan(request, pk):
    buat_surat = Surat.objects.get(id=pk)

    context = {'buat_surat': buat_surat}
    return render(request, 'surat/pdf_penghasilan.html', context)


#laporan perbulan
def LaporanBView(request):
    if 'BULAN' in request.GET:
        chek=request.GET['BULAN']
        tampil_data = Surat.objects.filter(BULAN=chek)
    else:
        tampil_data = Surat.objects.filter(BULAN=None)     

    context = {'tampil_data': tampil_data,}
    return render(request, 'surat/lp_perbulan.html',  context)      

#laporan alamat
def lp_penduduk(request):
    if 'ALAMAT' in request.GET:
        chek=request.GET['ALAMAT']
        tampil = Penduduk.objects.filter(ALAMAT=chek)
    else:
        tampil = Penduduk.objects.filter(ALAMAT=None)     

    context = {'tampil': tampil,}
    return render(request, 'surat/lp_penduduk.html',  context)    


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def tambahpetugas(request):
    form = PetugasForm()
    formpetugas = PetugasForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = username). first():
            messages.success(request, 'Nama Pengguna Sudah ada')
            return redirect('petugas')
        if password1 != password2:
            messages.success(request, 'Kata Sandi Tidak Sama! Silahkan Coba Kembali')
            return redirect('petugas')
        #user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        #user
        #group
        surat_petugas = Group.objects.get(name ='petugas')
        user.groups.add(surat_petugas)
        #group

        # petugas
        formsimpanpetugas = formpetugas.save()
        formsimpanpetugas.user = user
        formsimpanpetugas.save()
    context = {
        'menu' : 'Form Saya',
        'page' : 'form saya',
        'form' : form,
    }
    return render(request, 'surat/tambahpetugas.html', context)
    
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def petugas(request):
    tabelpetugas = Petugas.objects.all()
    context = {
        'menu' : 'Data Petugas',
        'page' : 'Halaman Data Petugas',
        'petugas' : tabelpetugas,
    }
    return render(request, 'surat/petugas.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['petugas'])
def editpetugas (request, pk):
    up_petugas = Petugas.objects.get(id=pk)
    editpetugas = PetugasForm(instance=up_petugas)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = PetugasForm(request.POST, instance=up_petugas)
        if formedit.is_valid:
            formedit.save()
            return redirect('petugas')
    context = {
        "menu" : 'editpetugas',
        "page" : 'Edit Petugas',
        "editpetugas" : editpetugas,
    }
    return render(request, 'surat/editpetugas.html', context)


@login_required(login_url='login')
def berandakepdes(request):
    datapenduduk = Penduduk.objects.all()
    list_surat = Surat.objects.all()
    total_penduduk = Penduduk.objects.count()
    total_kematian = datapenduduk.filter(KETERANGAN = 'MENINGGAL'). count()
    total_pindah= datapenduduk.filter(KETERANGAN = 'PINDAH'). count()
    total_surat = Surat.objects.count()
    total_mati= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kematian'). count()
    total_domisili= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Domisili'). count()
    total_covid = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Terdampak Covid'). count()
    total_usaha= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Usaha'). count()
    total_skkb = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kelakuan Baik'). count()
    total_sktm = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Tidak Mampu'). count()
    total_hilang = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kehilangan'). count()
    total_hasil = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Penghasilan'). count()
    context = {
        "menu" : 'Beranda',
        "page" : 'Selamat Datang di Aplikasi Layanan Surat',
        'dt_penduduk' : datapenduduk,
        'data_penduduk' : total_penduduk,
        'data_kematian' : total_kematian,
        'data_pendudukpindah' : total_pindah,

        'jumlah_surat' : total_surat,
        'surat_kematian' : total_mati,
        'surat_covid' : total_covid,
        'surat_domisili' : total_domisili,
        'surat_usaha' : total_usaha,
        'surat_skkb' : total_skkb,
        'surat_sktm' : total_sktm,
        'surat_hilang' : total_hilang,
        'surat_hasil' : total_hasil,

    }
    return render(request, 'surat/berandakepdes.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['kepdes'])
def pendudukkepdes(request):
    list_penduduk = Penduduk.objects.order_by('-NO_KK')
    filter_penduduk = PendudukFilter(request.GET, queryset=list_penduduk)     
    list_penduduk=filter_penduduk.qs
    halaman_tampil = Paginator(list_penduduk, 10)     
    halaman_url = request.GET.get('halaman',1)     
    halaman_penduduk = halaman_tampil.get_page(halaman_url)

    if halaman_penduduk.has_previous(): 
        url_previous = f'?halaman={halaman_penduduk.previous_page_number()}'    
    else:         
        url_previous = '' 
    if halaman_penduduk.has_next():         
        url_next = f'?halaman={halaman_penduduk.next_page_number()}'     
    else:         
        url_next = ''
    context = {
        "menu" : 'Data ',
        "page" : 'Data Penduduk',
        "tampil" : list_penduduk,         
        'halaman_list_penduduk':halaman_penduduk,
        'filter_list_penduduk': filter_penduduk,
        'previous' : url_previous,         
        'next' : url_next,
        
    }
    return render(request, 'surat/pendudukkepdes.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['kepdes'])
def jenissuratkepdes(request):
    list_jenissurat = Jenis_Surat.objects.order_by('-JENIS_SURAT')
    context = {
        "menu" : 'Jenis',
        "page" : 'Jenis Surat',
        "tampil" : list_jenissurat,
    }
    return render(request, 'surat/jenissuratkepdes.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['kepdes'])
def suratkepdes(request):
    list_surat = Surat.objects.order_by('-TANGGAL')
    filter_surat = SuratFilter(request.GET, queryset=list_surat)     
    list_surat = filter_surat.qs
    halaman_tampil = Paginator(list_surat, 10)     
    halaman_url = request.GET.get('halaman',1)     
    halaman_surat = halaman_tampil.get_page(halaman_url)

    if halaman_surat.has_previous(): 
        url_previous = f'?halaman={halaman_surat.previous_page_number()}'    
    else:         
        url_previous = '' 
    if halaman_surat.has_next():         
        url_next = f'?halaman={halaman_surat.next_page_number()}'     
    else:         
        url_next = ''
    context = {
        "menu" : 'Data ',
        "page" : 'Data Surat',
        "list" : list_surat,
        'halaman_list_surat':halaman_surat,
        'filter_list_surat': filter_surat,
        'previous' : url_previous,         
        'next' : url_next,
    }
    return render(request, 'surat/suratkepdes.html', context)


@login_required(login_url='login')
def berandamasyarakat(request):
    datapenduduk = Penduduk.objects.all()
    list_surat = Surat.objects.all()
    total_penduduk = Penduduk.objects.count()
    total_kematian = datapenduduk.filter(KETERANGAN = 'MENINGGAL'). count()
    total_pindah= datapenduduk.filter(KETERANGAN = 'PINDAH'). count()
    total_surat = Surat.objects.count()
    total_mati= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kematian'). count()
    total_covid = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Covid'). count()
    total_domisili = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Domisili'). count()
    total_usaha= list_surat.filter(JENIS_SURAT = 'Surat Keterangan Usaha'). count()
    total_skkb = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Kelakuan Baik'). count()
    total_sktm = list_surat.filter(JENIS_SURAT = 'Surat Keterangan Tidak Mampu'). count()
    total_hilang = list_surat.filter(JENIS_SURAT = 'Surang Keterangan Kehilangan '). count()
    total_penghasilan = list_surat.filter(JENIS_SURAT = 'Surang Keterangan Penghasilan '). count()
    context = {
        "menu" : 'Beranda',
        "page" : 'Selamat Datang di Aplikasi Layanan Surat',
        'dt_penduduk' : datapenduduk,
        'data_penduduk' : total_penduduk,
        'data_kematian' : total_kematian,
        'data_pendudukpindah' : total_pindah,

        'jumlah_surat' : total_surat,
        'surat_kematian' : total_mati,
        'surat_covid' : total_covid,
        'surat_domisili' : total_domisili,
        'surat_usaha' : total_usaha,
        'surat_skkb' : total_skkb,
        'surat_sktm' : total_sktm,
        'surat_hilang' : total_hilang,
        'surat_penghasilan' : total_penghasilan,

    }
    return render(request, 'surat/berandamasyarakat.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['masyarakat'])
def inputsuratmasyarakat(request):
    if request.method == 'POST':
        nama_lengkap= request.POST['nama_lengkap'],
        nik= request.POST['nik'],
        jenis_surat = request.POST['jenis_surat'],
        keterangan = request.POST['keterangan'],        
        catatan = request.POST['catatan'],
        no_telp= request.POST['no_telp'],

        Masyarakat.objects.create(
            nama_lengkap = nama_lengkap,
            nik = nik,
            jenis_surat = jenis_surat,
            keterangan = keterangan,
            catatan = catatan,
            no_telp = no_telp,
            
            
        )
        return redirect('/')
    return render(request, 'surat/inputsuratmasyarakat.html')