from django.shortcuts import render
from django.shortcuts import render,redirect
from . import models
from weasyprint import HTML
import datetime
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
     produkobj = models.produk.objects.get(id_produk=id)
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
  
def mitra(request):
    mitraobj = models.mitra.objects.all()
    return render(request, 'mitra.html', {
        'mitraobj' : mitraobj,
    })

def create_mitra(request):
    if request.method == "GET":
        return render(request, 'createmitra.html')
    else:
        nama_mitra = request.POST["nama_mitra"]
        alamat_mitra = request.POST["alamat_mitra"]
        nomor_mitra = request.POST["nomor_mitra"]
        tanggal_mulai_mitra = request.POST["tanggal_mulai_mitra"]
        durasi_kontrak = request.POST["durasi_kontrak"]
        luas_lahan = request.POST["luas_lahan"]

        newmitra = models.mitra(
            nama_mitra = nama_mitra,
            alamat_mitra = alamat_mitra,
            nomor_mitra = nomor_mitra,
            tanggal_mulai_mitra = tanggal_mulai_mitra,
            durasi_kontrak = durasi_kontrak,
            luas_lahan = luas_lahan   
        )
        newmitra.save()
        return redirect('mitra')

def update_mitra(request,id):
    mitraobj = models.mitra.objects.get(id_mitra=id)
    if request.method == "GET" :
        return render(request, 'updatemitra.html', {
            'mitraobj' : mitraobj,
        })
    else :
        mitraobj.nama_mitra = request.POST['nama_mitra']
        mitraobj.alamat_mitra = request.POST['alamat_mitra']
        mitraobj.nomor_mitra = request.POST['nomor_mitra']
        mitraobj.tanggal_mulai_mitra = request.POST['tanggal_mulai_mitra']
        mitraobj.durasi_kontrak = request.POST['durasi_kontrak']
        mitraobj.luas_lahan = request.POST['luas_lahan']
        mitraobj.save()
        return redirect('mitra')

def delete_mitra(request,id):
    mitraobj = models.mitra.objects.get(id_mitra=id)
    mitraobj.delete()
    return redirect('mitra')

def pembeli(request):
    pembeliobj = models.pembeli.objects.all()
    return render(request, 'pembeli.html', {
        'pembeliobj' : pembeliobj,
    })

def create_pembeli(request):
    if request.method == "GET":
        return render(request, 'createpembeli.html')
    else:
        nama_pembeli = request.POST["nama_pembeli"]
        nomor_pembeli = request.POST["nomor_pembeli"]
        alamat_pembeli = request.POST["alamat_pembeli"]

        newpembeli = models.pembeli(
            nama_pembeli = nama_pembeli,
            nomor_pembeli = nomor_pembeli,
            alamat_pembeli = alamat_pembeli,
        )
        newpembeli.save()
        return redirect('pembeli')

def update_pembeli(request,id):
    pembeliobj = models.pembeli.objects.get(id_pembeli=id)
    if request.method == "GET" :
        return render(request, 'updatepembeli.html', {
            'pembeliobj' : pembeliobj,
        })
    else :
        pembeliobj.nama_pembeli = request.POST['nama_pembeli']
        pembeliobj.nomor_pembeli = request.POST['nomor_pembeli']
        pembeliobj.alamat_pembeli = request.POST['alamat_pembeli']
        pembeliobj.save()
        return redirect('mitra')

def delete_pembeli(request,id):
    pembeliobj = models.pembeli.objects.get(id_pembeli=id)
    pembeliobj.delete()
    return redirect('pembeli')

def detail_jual(request):
    alldetailjualobj = models.detail_jual.objects.all()
    getdetailobj = models.detail_jual.objects.get(id_detailjual=1)
    return render(request, 'detailjual.html', {
        "alldetailjualobj" : alldetailjualobj,
        "getdetailobj" : getdetailobj,
    })

def create_detail_jual(request):
    if request.method == "GET":
        allpenjualanobj = models.penjualan.objects.all()
        allprodukobj = models.produk.objects.all()
        return render(request, 'createdetailpenjualan.html',{
            'datapenjualan' : allpenjualanobj, 'dataproduk' : allprodukobj
        })
    if request.method == "POST":
        id_penjualan = request.POST['id_penjualan']
        allpenjualanobj = models.penjualan.objects.get(id_penjualan=id_penjualan)
        id_produk = request.POST['id_produk']
        allprodukobj = models.produk.objects.get(id_produk=id_produk)
        jumlah = request.POST["jumlah"]

        newdetailjual = models.detail_jual(
            id_penjualan = allpenjualanobj,
            id_produk = allprodukobj,
            jumlah = jumlah
        )
        newdetailjual.save()

        return redirect('detailjual')

def update_detail_jual(request,id):
    detailjualobj = models.detail_jual.objects.get(id_detailjual=id)
    allpenjualanobj = models.penjualan.objects.all()
    allprodukobj = models.produk.objects.all()
    if request.method == "GET" :
        return render(request, 'updatedetailjual.html', {
            'alldetailjual' : detailjualobj, 'datapenjualan' : allpenjualanobj, 'dataproduk' : allprodukobj,
        })
    else :
        getidpenjualan = models.penjualan.objects.get(id_penjualan = request.POST['id_penjualan']) 
        getidproduk = models.produk.objects.get(id_produk = request.POST['id_produk'])
        detailjualobj.jumlah = request.POST['jumlah']
        detailjualobj.id_penjualan = getidpenjualan
        detailjualobj.id_produk = getidproduk
        detailjualobj.save()
        return redirect('detailjual')

def delete_detail_jual(request,id):
    detailjualobj = models.detail_jual.objects.get(id_detailjual=id)
    detailjualobj.delete()
    return redirect('detailjual')

def transaksi_lain(request):
    transaksi_lain_all = models.transaksi_lain.objects.all()
    
    return render(request, 'transaksi_lain.html',{
        'transaksi_lain_all' : transaksi_lain_all
    })

def create_transaksi_lain(request):
    if request.method == "GET":
        return render (request, "form_create_transaksi_lain.html")
    else:
        jenis_transaksi = request.POST["jenis_transaksi"]
        tanggal_transaksi = request.POST["tanggal_transaksi"]
        biaya = request.POST["biaya.html"]

        new_transaksi_lain = models.transaksi_lain(
            jenis_transaksi = jenis_transaksi,
            tanggal_transaksi = tanggal_transaksi,
            biaya = biaya
        )
        new_transaksi_lain.save()
        return redirect("transaksi_lain")
    
def update_transaksi_lain(request, id):
    transaksi_lain_all = models.transaksi_lain.objects.get(id_transaksi = id)
    if request.method == "GET":
        return render(request, "form_update_transaksi_lain.html",{
            'panen' : transaksi_lain_all})
    else :
        jenis_transaksi = request.POST["jenis_transaksi"]
        tanggal_transaksi = request.POST["tanggal_transaksi"]
        biaya = request.POST["biaya.html"]
        transaksi_lain_all.jenis_transaksi = jenis_transaksi
        transaksi_lain_all.tanggal_transaksi = tanggal_transaksi
        transaksi_lain_all.biaya = biaya
        transaksi_lain_all.save()
        return redirect('transaksi_lain')

def delete_transaksi_lain():
    transaksi_lain_all = models.transaksi_lain.get(id_transaksi=id)
    transaksi_lain_all.delete()
    return redirect('transaksi_lain')

def delete_panen():
    panen_obj = models.panen.objects.get(id_panen = id)
    panen_obj.delete()
    return redirect('panen')
   
def panen(request):
    allpanenobj = models.panen.objects.all()
    return render(request, 'panen.html', {"allpanenobj" : allpanenobj})

def create_panen(request):
    if request.method == 'GET':
        allmitraobj = models.mitra.objects.all()
        return render (request, "form_create_panen.html",{})
    if request.method == "POST":
        id_mitra = request.POST["id_mitra"]
        allmitraobj = models.mitra.objects.get(id_mitra)
        biaya_pembelian = request.POST["biaya_pembelian"]
        tanggal_panen = models.POST["tanggal_panen"]

        newpanen = models.panen(
            idmitra = allmitraobj,
            biaya_pembelian = biaya_pembelian,
            tanggal_panen = tanggal_panen
        )
        newpanen.save()

        return redirect('panen')

def update_panen(request, id):
    panen_obj = models.panen.objects.get(id_panen = id)
    if request.method == "GET":
        return render(request, "form_update_panen.html",{
            'panen' : panen_obj})
    else :
        id_mitra = request.POST['id_mitra']
        biaya_pembelian = request.POST['biaya_pembelian']
        tanggal_panen = request.POST['tanggal_panen']
        panen_obj.id_mitra = id_mitra
        panen_obj.biaya_pembelian = biaya_pembelian
        panen_obj.tanggal_panen = tanggal_panen
        panen_obj.save()
        return redirect('panen')

def delete_panen():
    panen_obj = models.panen.objects.get(id_panen = id)
    panen_obj.delete()
    return redirect('panen')

def penjualan(request):
    penjualanobj = models.penjualan.object.all()
    return render (request, 'penjualan.html',{
        'allpenjualan' : penjualanobj
    })

def createpenjualan(request,id):
    if request.method == "GET":
        filterpembeliobj = models.pembeli.object.filter(id_pembeli = id)
        return render (request, 'penjualan.html',{
            'datapembeli' : filterpembeliobj
        })
    elif request.method == 'POST':
        nama_pembeli = request.POST['nama_pembeli']
        nomor_pembeli = request.POST['nomor_pembeli']
        alamat_pembeli = request.POST['alamat_pembeli']

        total_penjualan = models.pembeli.object.all().count()
        newpembeli = models.pembeli(
            nama_pembeli = nama_pembeli,
            nomor_pembeli = nomor_pembeli,
            alamat_pembeli = alamat_pembeli
        ).save()
        pembeliobj = models.pembeli.all().last()
        newpenjualan = models.penjualan(
            tanggalpenjualan = tanggalpenjualan
        ).save()
        return redirect('penjualan')

def updatepenjualan(request,id):
    penjualanobj = models.penjualan.get(id_penjualan = id)
    if request.method == 'GET':
        return render(request, 'updatepenjualan.html',{
            'penjualanobj' : penjualanobj
        })
    else:
        tanggalpenjualan = request.POST['tanggalpenjualan']
        penjualanobj.tanggalpenjualan = tanggalpenjualan
        penjualanobj.save()
        return redirect ('penjualan')

def deletepenjualan(request, id):
    penjualanobj = models.penjualan.objects.get(id_penjualan = id)
    penjualanobj.delete()
    return redirect ('penjualan')

def komoditas(request):
    komoditasobj = models.komoditas.objects.all()
    return render(request, 'komoditas.html', {
        'komiditasobj' : komoditasobj
    })

def create_komoditas(request):
    if request.method == "GET":
        return render(request, 'createkomoditas.html')
    else:
        nama_komoditas = request.POST["namakomoditas"]
        satuan = request.POST["satuan"]
        kode_grade = request.POST["kodegrade"]
        harga_sewa = request.POST["hargasewa"]

        newkomoditas = models.komoditas(
            nama_komoditas = nama_komoditas,
            satuan = satuan,
            kode_grade = kode_grade,
            harga_sewa = harga_sewa,
        )
        newkomoditas.save()
        return redirect('komoditas')

def updatekomoditas(request, id):
    komoditasobj = models.komoditas.objects.get(idkomoditas = id)
    if request.method == "GET":
        return render(request, 'updatekomoditas.html', {
            'allkomoditas' : komoditasobj,
        })
    else:
        komoditasobj.namakomoditas = request.POST['namakomoditas']
        komoditasobj.satuan = request.POST["satuan"]
        komoditasobj.kodegrade = request.POST['kodegrade']
        komoditasobj.hargasewa = request.POST['hargasewa']
        komoditasobj.save()
        return redirect('komoditas')

def deletekomoditas(request,id):
    komoditasobj = models.komoditas.objects.get(idkomoditas = id)
    komoditasobj.delete()
    return redirect('komoditas')
