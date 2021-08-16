from django.urls import path 
from . import views

urlpatterns = [   
    #url penduduk  
    path('', views.beranda, name='beranda'),
    path('penduduk/', views.penduduk, name='penduduk'),
    path('tambahpenduduk/', views.tambahpenduduk, name='tambahpenduduk'),
    path('editpenduduk/<str:pk>', views.editpenduduk, name='editpenduduk'),
    path('export-excel/', views.export, name='export'),
    path('upload/', views.upload, name='upload'),

    #url jenis surat
    path('jenissurat/', views.jenissurat, name='jenissurat'),
    path('tambahjenissurat/', views.tambahjenissurat, name='tambahjenissurat'),

    #url laynan surat
    path('layanansurat', views.layanansurat, name='layanansurat'),
    path('inputsurat', views.inputsurat, name='inputsurat'),
    path('ambilnik/', views.ambilnik, name='ambilnik'),
    
    #url surat
    path('laporansurat/', views.surat, name='surat'),
    path('editsurat/<str:pk>', views.editsurat, name='editsurat'),
    path('laporan/', views.LaporanBView, name='laporan'),
    path('lp_penduduk/', views.lp_penduduk, name='lp_penduduk'),

    path('login-page/', views.loginPage, name='login'),
    path('logout-page/', views.logoutPage, name='logout'),


    path('petugas', views.petugas, name='petugas'),
    path('tambahpetugas/', views.tambahpetugas, name='tambahpetugas'),
    path('editpetugas/<str:pk>', views.editpetugas, name='editpetugas'),



    #kepdes
    path('beranda-kepdes', views.berandakepdes, name='berandakepdes'),
    path('penduduk-kepdes', views.pendudukkepdes, name='pendudukkepdes'),
    path('jenissurat-kepdes', views.jenissuratkepdes, name='jenissuratkepdes'),
    path('surat-kepdes', views.suratkepdes, name='suratkepdes'),
    # path('profilkepdes', views.profilkepdes, name='profilkepdes'),

    
    path('berandamasyarakat', views.berandamasyarakat, name='berandamasyarakat'),
    path('inputsuratmasyarakat/', views.inputsuratmasyarakat, name='inputsuratmasyarakat'),


    #pdf surat
    path('pdf_usaha/<str:pk>', views.pdf_usaha, name='pdf_usaha'),
    path('pdf_kematian/<str:pk>', views.pdf_kematian, name='pdf_kematian'),
    path('pdf_domisili/<str:pk>', views.pdf_domisili, name='pdf_domisili'),
    path('pdf_kehilangan/<str:pk>', views.pdf_kehilangan, name='pdf_kehilangan'),
    path('pdf_penghasilan/<str:pk>', views.pdf_penghasilan, name='pdf_penghasilan'),
    path('pdf_tidakmampu/<str:pk>', views.pdf_tidakmampu, name='pdf_tidakmampu'),
    path('pdf_covid/<str:pk>', views.pdf_covid, name='pdf_covid'),
    path('pdf_kelakuanbaik/<str:pk>', views.pdf_kelakuanbaik, name='pdf_kelakuanbaik'),

 
   
] 



