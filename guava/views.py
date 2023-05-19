from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
# Create your views here.

def produk(request):
     allprodukobj = models.produk.objects.all()

     return render (request, 'produk.html',{
          'allprodukobj' : allprodukobj,
          })

def create_produk(request):
     if request.method == "GET" :
          return render(request, 'create produk.html')
     else:
          nama_produk = request.POST['nama_produk']
          satuan_produk = request.POST['satuan_produk']
          harga_produk = request.POST['harga_produk']

          models.produk(
               namaproduk = nama_produk,
               satuanproduk = satuan_produk,
               hargaproduk = harga_produk,
          ).save()
          return redirect('produk')

def update_produk(request,id):
     produkobj = models.produk.objects.get(idobat=id)
     if request.method == "GET":
          return render(request, 'update produk.html', {
               'produkobj' : produkobj
               })
     else:
          produkobj.namaproduk = request.POST['nama_produk']
          produkobj.satuanproduk = request.POST['satuan_produk']
          produkobj.hargaproduk= request.POST['harga_produk']
          produkobj.save()
          return redirect('produk')

def delete_produk(request, id):
     produkobj = models.produk.objects.get(id_produk=id)
     produkobj.delete()
     return redirect('produk')

def detail_panen(request):
     alldetailpanenobj = models.detail_panen.objects.all()
     getdetailobj = models.detail_panen.objects.get(id_detailpanen=1)
     return render(request, 'detail panen.html', {
          "alldetailpanenobj" : alldetailpanenobj,
          "getdetailobj" : getdetailobj,
     })

def create_detailpanen(request):
     if request.method == "GET":
          allpanenobj = models.panen.objects.all()
          allkomoditasobj = models.komoditas.objects.all()
          return render(request, 'create detail panen.html',{
               'datapanen' : allpanenobj, 'datakomoditas' : allkomoditasobj
          })
     if request.method == "POST":
          idpanen = request.POST['id_panen']
          allpanenobj = models.panen.objects.get(id_panen=idpanen)
          id_komoditas = request.POST['id_komoditas']
          allkomoditasobj = models.komoditas.objects.get(id_komoditas=id_komoditas)
          jumlahpanen = request.POST["jumlahpanen"]
          tanggalkadaluwarsa = request.POST["tanggalkadaluwarsa"]

     models.detail_panen(
               idpanen = allpanenobj,
               id_komoditas = allkomoditasobj,
               jumlahpanen = jumlahpanen,
               tanggalkadaluwarsa = tanggalkadaluwarsa
          ).save()

     return redirect('detailpanen')

def update_detailpanen(request,id):
     detailpanenobj = models.detail_panen.objects.get(id_detailjual=id)
     allpanenobj = models.panen.objects.all()
     allkomoditasobj = models.komoditas.objects.all()
     if request.method == "GET" :
          return render(request, 'updatedetailpanen.html', {
               'alldetailpanen' : detailpanenobj, 'datapanen' : allpanenobj, 'datakomoditas' : allkomoditasobj,
          })
     else :
          getidpanen = models.panen.objects.get(idpanen = request.POST['id_panen']) 
          getidkomoditas = models.komoditas.objects.get(id_komodiras= request.POST['id_komoditas'])
          detailpanenobj.jumlahpanen = request.POST['jumlahpanen']
          detailpanenobj.idpanen = getidpanen
          detailpanenobj.idkomoditas = getidkomoditas
          detailpanenobj.save()
          return redirect('detailpanen')

def delete_detailpanen(request,id):
     detailpanenobj = models.detail_panen.objects.get(id_detailpanen=id)
     detailpanenobj.delete()
     return redirect('detailpanen')
