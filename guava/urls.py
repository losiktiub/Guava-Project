from django.urls import path
from . import views

urlpatterns = [
    path('produk', views.produk,name='produk'),
    path('createproduk', views.create_produk,name='createproduk'),
    path('updateproduk/<str:id>', views.update_produk,name='updateproduk'),
    path('deleteproduk/<str:id>', views.delete_produk,name='deleteproduk'),
    path('detailpanen', views.detail_panen,name='detailpanen'),
    path('createdetailpanen', views.create_detailpanen,name='createdetailpanen'),
    path('updatedetailpanen/<str:id>', views.update_detailpanen,name='updatedetailpanen'),
    path('deletedetailpanen/<str:id>', views.delete_detailpanen,name='deletedetailpanen'),
    path('mitra', views.mitra,name='mitra'),
    path('createmitra', views.create_mitra,name='createmitra'),
    path('updatemitra/<str:id>', views.update_mitra,name='updatemitra'),
    path('deletemitra/<str:id>', views.delete_mitra,name='deletemitra'),
    path('pembeli', views.pembeli,name='pembeli'),
    path('createpembeli', views.create_pembeli,name='createpembeli'),
    path('updatepembeli/<str:id>', views.update_pembeli,name='updatepembeli'),
    path('deletepembeli/<str:id>', views.delete_pembeli,name='deletepembeli'),
    path('detailjual', views.detail_jual,name='detailjual'),
    path('createdetailjual', views.create_detail_jual,name='createdetailjual'),
    path('updatedetailjual/<str:id>', views.update_detail_jual,name='updatedetailjual'),
    path('deletedetailjual/<str:id>', views.delete_detail_jual,name='deletedetailjual'),
    path('transaksilain', views.transaksi_lain,name='transaksilain'),
    path('createtransaksilain', views.create_transaksi_lain,name='createtransaksilain'),
    
    


]
