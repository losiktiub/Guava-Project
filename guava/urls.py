from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name="home"),
    path('',views.loginview, name='login'),
    path('performlogin',views.performlogin,name="performlogin"),
    path('performlogout',views.performlogout,name="performlogout"),
    path('produk/', views.produk,name='produk'),
    path('produk/createproduk', views.create_produk,name='createproduk'),
    path('produk/updateproduk/<str:id>', views.update_produk,name='updateproduk'),
    path('deleteproduk/<str:id>', views.delete_produk,name='deleteproduk'),
    path('detailpanen', views.detail_panen,name='detailpanen'),
    path('createdetailpanen', views.create_detailpanen,name='createdetailpanen'),
    path('updatedetailpanen/<str:id>', views.update_detailpanen,name='updatedetailpanen'),
    path('deletedetailpanen/<str:id>', views.delete_detailpanen,name='deletedetailpanen'),
    path('mitra/', views.mitra,name='mitra'),
    path('mitra/createmitra', views.create_mitra,name='createmitra'),
    path('mitra/updatemitra/<str:id>', views.update_mitra,name='updatemitra'),
    path('deletemitra/<str:id>', views.delete_mitra,name='deletemitra'),
    path('pembeli/', views.pembeli,name='pembeli'),
    path('pembeli/createpembeli', views.create_pembeli,name='createpembeli'),
    path('pembeli/updatepembeli/<str:id>', views.update_pembeli,name='updatepembeli'),
    path('deletepembeli/<str:id>', views.delete_pembeli,name='deletepembeli'),
    path('detailjual/', views.detail_jual,name='detailjual'),
    path('detailjual/createdetailjual', views.create_detail_jual,name='createdetailjual'),
    path('detailjual/updatedetailjual/<str:id>', views.update_detail_jual,name='updatedetailjual'),
    path('deletedetailjual/<str:id>', views.delete_detail_jual,name='deletedetailjual'),
    path('transaksilain', views.transaksi_lain,name='transaksilain'),
    path('createtransaksilain', views.create_transaksi_lain,name='createtransaksilain'),
    path('penjualan/', views.penjualan,name='penjualan'),
    path('penjualan/createpenjualan', views.create_penjualan,name='createpenjualan'),
    path('penjualan/updatepenjualan/<str:id>', views.updatepenjualan,name='updatepenjualan'),
    path('deletepenjualan/<str:id>', views.deletepenjualan,name='deletepenjualan'),
    path('komoditas/', views.komoditas,name='komoditas'),
    path('komoditas/createkomoditas', views.create_komoditas,name='createkomoditas'),
    path('komoditas/updatekomoditas/<str:id>', views.updatekomoditas,name='updatekomoditas'),
    path('deletekomoditas/<str:id>', views.deletekomoditas,name='deletekomoditas'),
    path('panen/', views.panen,name='panen'),
    path('panen/createpanen', views.create_panen,name='createpanen'),
    path('panen/updatepanen/<str:id>', views.update_panen,name='updatepanen'),
    path('deletepanen/<str:id>', views.delete_panen,name='deletepanen'),






]
