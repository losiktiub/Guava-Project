from django.shortcuts import render
from django.shortcuts import render,redirect
from . import models
from weasyprint import HTML
import datetime
from datetime import datetime
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib import messages
from guava.decorators import role_required
# Create your views here.

@login_required
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'loginsiam.html')
    else:
        return render(request, 'mitra.html')

    
@login_required
def logoutview(request):
    logout(request)
    messages.info(request,"Berhasil Logout")
    return redirect('login')

def loginview(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return render(request,"loginsiam.html")
    
def performlogin(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        print(request)
        username_login = request.POST['username']
        # print(username)
        password_login = request.POST['password']
        # print(username)
        userobj = authenticate(request, username=username_login,password=password_login)
        print(userobj)
        if userobj is not None:
            login(request, userobj)
            messages.success(request,"Login success")
            return redirect("home")
        else:
            messages.error(request,"Username atau Password salah !!!")
            return redirect("login")
        
@login_required
def performlogout(request):
    logout(request)
    print("Anda keluar")
    return redirect("login")

@login_required
def produk(request):
    allprodukobj = models.produk.objects.all()

    return render (request, 'produk/produk.html',{
        'allprodukobj' : allprodukobj,
        })

@login_required
def create_produk(request):
    if request.method == "GET" :
        return render(request, 'produk/createproduk.html')
    else:
        nama_produk = request.POST['namaproduk']
        satuan_produk = request.POST['satuanproduk']
        harga_produk = request.POST['hargaproduk']

        models.produk(
            namaproduk = nama_produk,
            satuanproduk = satuan_produk,
            hargaproduk = harga_produk,
        ).save()
        return redirect('produk')

@login_required
def update_produk(request,id):
    produkobj = models.produk.objects.get(id_produk=id)
    if request.method == "GET":
        return render(request, 'produk/updateproduk.html', {
            'produkobj' : produkobj
            })
    else:
        produkobj.namaproduk = request.POST['namaproduk']
        produkobj.satuanproduk = request.POST['satuanproduk']
        produkobj.hargaproduk= request.POST['hargaproduk']
        produkobj.save()
        return redirect('produk')

@login_required
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

@login_required
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

@login_required
def delete_detailpanen(request,id):
    detailpanenobj = models.detail_panen.objects.get(id_detailpanen=id)
    detailpanenobj.delete()
    return redirect('detailpanen')

@login_required
@role_required(allowed_roles=['Admin', 'Pegawai'])
def mitra(request):
    mitraobj = models.mitra.objects.all()
    # is_admin = request.user.groups.filter(name='Admin').exists()
    # is_pegawai = request.user.groups.filter(name='Pegawai').exists()

    return render(request, 'mitra/mitra.html', {
        'mitraobj' : mitraobj,
        'is_admin': request.is_admin,
        'is_editor': request.is_pegawai
    })

@login_required
@role_required(allowed_roles=['Admin'])
def create_mitra(request):
    if request.method == "GET":
        return render(request, 'mitra/createmitra.html')
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

@login_required
def update_mitra(request,id):
    mitraobj = models.mitra.objects.get(id_mitra = id)
    if request.method == "GET" :
        tanggal = datetime.strftime(mitraobj.tanggal_mulai_mitra, '%Y-%m-%d')
        return render(request, 'mitra/updatemitra.html', {
            'mitraobj' : mitraobj,
            'tanggal' : tanggal
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

@login_required
def delete_mitra(request,id):
    mitraobj = models.mitra.objects.get(id_mitra = id)
    mitraobj.delete()
    return redirect('mitra')

def pembeli(request):
    pembeliobj = models.pembeli.objects.all()
    return render(request, 'pembeli/pembeli.html', {
        'pembeliobj' : pembeliobj,
    })

@login_required
def create_pembeli(request):
    if request.method == "GET":
        return render(request, 'pembeli/createpembeli.html')
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

@login_required
def update_pembeli(request,id):
    pembeliobj = models.pembeli.objects.get(id_pembeli=id)
    if request.method == "GET" :
        return render(request, 'pembeli/updatepembeli.html', {
            'pembeliobj' : pembeliobj,
        })
    else :
        pembeliobj.nama_pembeli = request.POST['nama_pembeli']
        pembeliobj.nomor_pembeli = request.POST['nomor_pembeli']
        pembeliobj.alamat_pembeli = request.POST['alamat_pembeli']
        pembeliobj.save()
        return redirect('pembeli')

@login_required
def delete_pembeli(request,id):
    pembeliobj = models.pembeli.objects.get(id_pembeli=id)
    pembeliobj.delete()
    return redirect('pembeli')

@login_required
def detail_jual(request):
    alldetailjualobj = models.detail_jual.objects.all()
    # getdetailobj = models.detail_jual.objects.get(id_detailjual=1)
    return render(request, 'detailjual/detailjual.html', {
        "alldetailjualobj" : alldetailjualobj,
        # "getdetailobj" : getdetailobj,
    })

@login_required
def create_detail_jual(request):
    if request.method == "GET":
        allpenjualanobj = models.penjualan.objects.all()
        allprodukobj = models.produk.objects.all()
        return render(request, 'detailjual/createdetailjual.html', {
            'datapenjualan': allpenjualanobj,
            'dataproduk' : allprodukobj
            })

    elif request.method == "POST":
        id_penjualan = request.POST['id_penjualan']
        id_produk= request.POST['id_produk']
        jumlah = request.POST['jumlah']

        newdetailjual = models.detail_jual.objects.create(
            id_penjualan_id=id_penjualan,
            id_produk_id = id_produk,
            jumlah = jumlah
        )

        return redirect('detailjual')
# def create_detail_jual(request):
#     if request.method == "GET":
#         allpenjualanobj = models.penjualan.objects.all()
#         allprodukobj = models.produk.objects.all()
#         return render(request, 'detailjual/createdetailjual.html',{
#             'datapenjualan' : allpenjualanobj, 'dataproduk' : allprodukobj
#         })
#     if request.method == "POST":
#         id_penjualan = request.POST['id_penjualan']
#         allpenjualanobj = models.penjualan.objects.get(id_penjualan=id_penjualan)
#         id_produk = request.POST['id_produk']
#         allprodukobj = models.produk.objects.get(id_produk=id_produk)
#         jumlah = request.POST["jumlah"]

#         newdetailjual = models.detail_jual(
#             id_penjualan = allpenjualanobj,
#             id_produk = allprodukobj,
#             jumlah = jumlah
#         )
#         newdetailjual.save()

#         return redirect('detailjual')

@login_required
def update_detail_jual(request,id):
    detailjualobj = models.detail_jual.objects.get(id_detailjual=id)
    allpenjualanobj = models.penjualan.objects.all()
    allprodukobj = models.produk.objects.all()
    if request.method == "GET" :
        return render(request, 'detailjual/updatedetailjual.html', {
            'detailjualobj' : detailjualobj, 
            'datapenjualan' : allpenjualanobj,
            'dataproduk' : allprodukobj,
        })
    else :
        id_penjualan = request.POST['id_penjualan']
        id_produk = request.POST['id_produk']
        getidpenjualan = models.penjualan.objects.get(id_penjualan = id_penjualan   ) 
        getidproduk = models.produk.objects.get(id_produk = id_produk)
        detailjualobj.jumlah = request.POST['jumlah']
        detailjualobj.id_penjualan = getidpenjualan
        detailjualobj.id_produk = getidproduk
        detailjualobj.save()
        return redirect('detailjual')

@login_required
def delete_detail_jual(request,id):
    detailjualobj = models.detail_jual.objects.get(id_detailjual=id)
    detailjualobj.delete()
    return redirect('detailjual')

@login_required
def transaksi_lain(request):
    transaksi_lain_all = models.transaksi_lain.objects.all()
    
    return render(request, 'transaksi_lain.html',{
        'transaksi_lain_all' : transaksi_lain_all
    })

@login_required
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
    
@login_required
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
    
@login_required
def delete_transaksi_lain():
    transaksi_lain_all = models.transaksi_lain.get(id_transaksi=id)
    transaksi_lain_all.delete()
    return redirect('transaksi_lain')

@login_required
def delete_panen():
    panen_obj = models.panen.objects.get(id_panen = id)
    panen_obj.delete()
    return redirect('panen')

@login_required
def panen(request):
    allpanenobj = models.panen.objects.all()
    return render(request, 'panen/panen.html', {
        "allpanenobj" : allpanenobj
        })

@login_required
def create_panen(request):
    if request.method == 'GET':
        allmitraobj = models.mitra.objects.all()
        return render(request, 'panen/createpanen.html', {
            'datamitra': allmitraobj
        })

    elif request.method == "POST":
        id_mitra = request.POST["id_mitra"]
        biaya_pembelian = request.POST["biaya_pembelian"]

        tanggal_panen= request.POST["tanggal_panen"]

        newpanen = models.panen.objects.create(
            id_mitra_id=id_mitra,
            biaya_pembelian=biaya_pembelian,
            tanggal_panen=tanggal_panen
        )

        return redirect('panen')

# def create_panen(request):
#     if request.method == 'GET':
#         allmitraobj = models.mitra.objects.all()
#         return render (request, "panen/createpanen.html",{})
#     if request.method == "POST":
#         id_mitra = request.POST["id_mitra"]
#         allmitraobj = models.mitra.objects.get(id_mitra)
#         biaya_pembelian = request.POST["biaya_pembelian"]
#         tanggal_panen = models.POST["tanggal_panen"]

#         newpanen = models.panen(
#             idmitra = allmitraobj,
#             biaya_pembelian = biaya_pembelian,
#             tanggal_panen = tanggal_panen
#         )
#         newpanen.save()

#         return redirect('panen')

@login_required
def update_panen(request, id):
    panenobj = models.panen.objects.get(id_panen = id)
    if request.method == "GET":
        allmitraobj = models.mitra.objects.all()
        tanggal = datetime.strftime(panenobj.tanggal_panen, '%Y-%m-%d')
        return render(request, "panen/updatepanen.html",{
            'panenobj' : panenobj,
            'datamitra' : allmitraobj,
            'tanggal' : tanggal
            })
    else :
        id_mitra = request.POST['id_mitra']
        getidmitra = models.mitra.objects.get(id_mitra=id_mitra)
        panenobj.biaya_pembelian = request.POST['biaya_pembelian']
        panenobj.tanggal_panen = request.POST['tanggal_panen']
        panenobj.id_mitra = getidmitra
        panenobj.save()
        return redirect('panen')

@login_required
def delete_panen():
    panen_obj = models.panen.objects.get(id_panen = id)
    panen_obj.delete()
    return redirect('panen')

@login_required
def penjualan(request):
    penjualanobj = models.penjualan.objects.all()
    return render (request, 'penjualan/penjualan.html',{
        'penjualanobj' : penjualanobj
    })

@login_required
def create_penjualan(request):
    if request.method == "GET":
        allpembeliobj = models.pembeli.objects.all()
        return render(request, 'penjualan/createpenjualan.html', {
            'datapembeli': allpembeliobj
            })

    elif request.method == "POST":
        idpembeli = request.POST['idpembeli']
        tanggalpenjualan = request.POST['tanggalpenjualan']

        newpenjualan = models.penjualan.objects.create(
            idpembeli_id=idpembeli,
            tanggalpenjualan=tanggalpenjualan
        )

        return redirect('penjualan')
# def create_penjualan(request):
#     if request.method == "GET":
#         allpembeliobj = models.pembeli.objects.all()
#         return render(request, 'createpenjualan.html', {
#             'datapembeli': allpembeliobj
#             })
#     elif request.method == 'POST':
#         idpembeli = request.POST['idpembeli']
#         getpembeliobj = models.pembeli.objects.get(id_pembeli = idpembeli)
#         tanggalpenjualan = request.POST['tanggalpenjualan']

#         newpenjualan =  models.penjualan(
#             idpembeli = getpembeliobj,
#             tanggalpenjualan = tanggalpenjualan
#         )
#         newpenjualan.save()
#         return redirect('penjualan')


# def createpenjualan(request,id):
#     if request.method == "GET":
#         filterpembeliobj = models.pembeli.object.filter(id_pembeli = id)
#         return render (request, 'penjualan.html',{
#             'datapembeli' : filterpembeliobj
#         })
#     elif request.method == 'POST':
#         nama_pembeli = request.POST['nama_pembeli']
#         nomor_pembeli = request.POST['nomor_pembeli']
#         alamat_pembeli = request.POST['alamat_pembeli']

#         total_penjualan = models.pembeli.object.all().count()
#         models.pembeli(
#             nama_pembeli = nama_pembeli,
#             nomor_pembeli = nomor_pembeli,
#             alamat_pembeli = alamat_pembeli
#         ).save()
#         pembeliobj = models.pembeli.all().last()
#         # newpenjualan = models.penjualan(
#         #     tanggalpenjualan = tanggalpenjualan
#         # ).save()
#         return redirect('penjualan')

@login_required
def updatepenjualan(request,id):
    penjualanobj = models.penjualan.objects.get(id_penjualan=id)
    if request.method == "GET":
        allpembeliobj = models.pembeli.objects.all()
        tanggal = datetime.strftime(penjualanobj.tanggalpenjualan, '%Y-%m-%d')
        return render(request, 'penjualan/updatepenjualan.html', {
            'penjualanobj' : penjualanobj,
            'datapembeli' : allpembeliobj,
            'tanggal' : tanggal
        })
    else:
        idpembeli = request.POST['idpembeli']
        getidpembeli = models.pembeli.objects.get(id_pembeli=idpembeli)
        penjualanobj.tanggalpenjualan = request.POST['tanggalpenjualan']
        penjualanobj.idpembeli = getidpembeli
        penjualanobj.save()
        return redirect('penjualan')
        
# def updatepenjualan(request,id):
#     penjualanobj = models.penjualan.get(id_penjualan = id)
#     if request.method == 'GET':
#         return render(request, 'updatepenjualan.html',{
#             'penjualanobj' : penjualanobj
#         })
#     else:
#         tanggalpenjualan = request.POST['tanggalpenjualan']
#         penjualanobj.tanggalpenjualan = tanggalpenjualan
#         penjualanobj.save()
#         return redirect ('penjualan')

@login_required
def deletepenjualan(request, id):
    penjualanobj = models.penjualan.objects.get(id_penjualan = id)
    penjualanobj.delete()
    return redirect ('penjualan')

@login_required
def komoditas(request):
    komoditasobj = models.komoditas.objects.all()
    return render(request, 'komoditas/komoditas.html', {
        'komoditasobj' : komoditasobj
    })

@login_required
def create_komoditas(request):
    if request.method == "GET":
        return render(request, 'komoditas/createkomoditas.html')
    else:
        nama_komoditas = request.POST["nama_komoditas"]
        satuan = request.POST["satuan"]
        kode_grade = request.POST["kode_grade"]
        harga_sewa = request.POST["harga_sewa"]

        newkomoditas = models.komoditas(
            nama_komoditas = nama_komoditas,
            satuan = satuan,
            kode_grade = kode_grade,
            harga_sewa = harga_sewa,
        )
        newkomoditas.save()
        return redirect('komoditas')

@login_required
def updatekomoditas(request, id):
    komoditasobj = models.komoditas.objects.get(id_komoditas = id)
    if request.method == "GET":
        return render(request, 'komoditas/updatekomoditas.html', {
            'komoditasobj' : komoditasobj,
        })
    else:
        komoditasobj.nama_komoditas = request.POST['nama_komoditas']
        komoditasobj.satuan = request.POST["satuan"]
        komoditasobj.kode_grade = request.POST['kode_grade']
        komoditasobj.harga_sewa = request.POST['harga_sewa']
        komoditasobj.save()
        return redirect('komoditas')

@login_required
def deletekomoditas(request,id):
    komoditasobj = models.komoditas.objects.get(id_komoditas = id)
    komoditasobj.delete()
    return redirect('komoditas')
