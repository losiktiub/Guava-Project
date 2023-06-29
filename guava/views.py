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
        return render(request, 'mitra/mitra.html')

@login_required
def logoutview(request):
    logout(request)
    messages.info(request,"Berhasil Logout")
    return redirect('login')

def loginview(request):
    if request.user.is_authenticated:
        return redirect("mitra")
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
            return redirect("mitra")
        else:
            messages.error(request,"Username atau Password salah !!!")
            return redirect("login")
        
@login_required
def performlogout(request):
    logout(request)
    print("Anda keluar")
    return redirect("login")

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
        tanggal_panen= request.POST["tanggal_panen"]

        newpanen = models.panen.objects.create(
            id_mitra_id=id_mitra,
            tanggal_panen=tanggal_panen
        )

        return redirect('panen')

@login_required
def update_panen(request, id):
    panenobj = models.panen.objects.get(id_panen = id)
    if request.method == "GET":
        allmitraobj = models.mitra.objects.all()
        tanggal= datetime.strftime(panenobj.tanggal_panen, '%Y-%m-%d')
        return render(request, "panen/updatepanen.html",{
            'panenobj' : panenobj,
            'datamitra' : allmitraobj,
            'tanggal' : tanggal
            })
    else :
        id_mitra = request.POST['id_mitra']
        getidmitra = models.mitra.objects.get(id_mitra=id_mitra)
        panenobj.tanggal_panen = request.POST['tanggal_panen']
        panenobj.id_mitra = getidmitra
        panenobj.save()
        return redirect('panen')

@login_required
def delete_panen(request,id):
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
        return render(request, 'penjualan/createpenjualan.html', {
            })

    elif request.method == "POST":
        tanggalpenjualan = request.POST['tanggalpenjualan']

        newpenjualan = models.penjualan.objects.create(
            tanggalpenjualan=tanggalpenjualan
        )

        return redirect('penjualan')

@login_required
def updatepenjualan(request,id):
    penjualanobj = models.penjualan.objects.get(id_penjualan=id)
    if request.method == "GET":
        tanggal = datetime.strftime(penjualanobj.tanggalpenjualan, '%Y-%m-%d')
        return render(request, 'penjualan/updatepenjualan.html', {
            'penjualanobj' : penjualanobj,
            'tanggal' : tanggal
        })
    else:
        penjualanobj.tanggalpenjualan = request.POST['tanggalpenjualan']
        penjualanobj.save()
        return redirect('penjualan')

@login_required
def deletepenjualan(request, id):
    penjualanobj = models.penjualan.objects.get(id_penjualan = id)
    penjualanobj.delete()
    return redirect ('penjualan')

@login_required
def transaksi_lain(request):
    transaksi_lain_all = models.transaksi_lain.objects.all()
    
    return render(request, 'transaksilain/transaksilain.html',{
        'transaksilainobj' : transaksi_lain_all
    })

@login_required
def create_transaksi_lain(request):
    if request.method == "GET":
        return render (request, "transaksilain/createtransaksilain.html")
    else:
        jenis_transaksi = request.POST["jenis_transaksi"]
        tanggal_transaksi = request.POST["tanggal_transaksi"]
        biaya = request.POST["biaya"]

        new_transaksi_lain = models.transaksi_lain(
            jenis_transaksi = jenis_transaksi,
            tanggal_transaksi = tanggal_transaksi,
            biaya = biaya
        )
        new_transaksi_lain.save()
        return redirect("transaksilain")
    
@login_required
def update_transaksi_lain(request, id):
    transaksi_lain_all = models.transaksi_lain.objects.get(id_transaksi = id)
    if request.method == "GET":
        tangal = datetime.strftime(transaksi_lain_all.tanggal_transaksi, '%Y-%m-%d')
        return render(request, "transaksilain/updatetransaksilain.html",{
            'transaksilainobj' : transaksi_lain_all, 
            'tanggal' : tangal
            })
    else :
        jenis_transaksi = request.POST["jenis_transaksi"]
        tanggal_transaksi = request.POST["tanggal_transaksi"]
        biaya = request.POST["biaya"]
        transaksi_lain_all.jenis_transaksi = jenis_transaksi
        transaksi_lain_all.tanggal_transaksi = tanggal_transaksi
        transaksi_lain_all.biaya = biaya
        transaksi_lain_all.save()
        return redirect('transaksilain')
    
@login_required
def delete_transaksi_lain(request,id):
    transaksi_lain_all = models.transaksi_lain.objects.get(id_transaksi=id)
    transaksi_lain_all.delete()
    return redirect('transaksilain')

# Grade
def grade(request):
    gradeobj = models.grade.objects.all()
    return render(request, 'grade/grade.html', {
        'gradeobj' : gradeobj
    })

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

        newkomoditas = models.komoditas(
            nama_komoditas = nama_komoditas,
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
        komoditasobj.save()
        return redirect('komoditas')

@login_required
def deletekomoditas(request,id):
    komoditasobj = models.komoditas.objects.get(id_komoditas = id)
    komoditasobj.delete()
    return redirect('komoditas')

def detailkomoditas(request):
    detailkomoditasobj = models.detail_komoditas.objects.all()
    return render(request, 'detailkomoditas/detailkomoditas.html', {
        'detailkomoditasobj' : detailkomoditasobj
    } )

from django.shortcuts import render, redirect

def create_detailkomoditas(request):
    if request.method == 'GET':
        allgradeobj = models.grade.objects.all()
        allkomoditasobj = models.komoditas.objects.all()
        return render(request, 'detailkomoditas/createdetailkomoditas.html',{
            'datagrade' : allgradeobj,
            'datakomoditas' : allkomoditasobj})
    
    elif request.method == 'POST':
        id_grade = request.POST['id_grade']
        id_komoditas = request.POST['id_komoditas']
        harga_beli = request.POST['harga_beli']
        harga_jual = request.POST['harga_jual']

        # Simpan detail komoditas
        new_detailkomoditas = models.detail_komoditas.objects.create(
            id_grade_id = id_grade,
            id_komoditas_id = id_komoditas,
            harga_beli=harga_beli, 
            harga_jual=harga_jual
            )

        return redirect('detailkomoditas')

def update_detailkomoditas(request, id):
    alldetailkomoditasobj = models.detail_komoditas.objects.get(id_detailkomoditas=id)
    allgradeobj = models.grade.objects.all()
    allkomoditasobj = models.komoditas.objects.all()

    if request.method == "GET":
        return render(request, "detailkomoditas/updatedetailkomoditas.html", {
            'detailkomoditasobj': alldetailkomoditasobj,
            'datagrade': allgradeobj,
            'datakomoditas': allkomoditasobj
        })
    else:
        id_grade = request.POST['id_grade']
        getidgrade = models.grade.objects.get(id_grade=id_grade)
        id_komoditas = request.POST['id_komoditas']
        getidkomoditas = models.komoditas.objects.get(id_komoditas=id_komoditas)
        alldetailkomoditasobj.harga_beli = request.POST['harga_beli']
        alldetailkomoditasobj.harga_jual = request.POST['harga_jual']
        alldetailkomoditasobj.id_komoditas = getidkomoditas
        alldetailkomoditasobj.id_grade = getidgrade
        alldetailkomoditasobj.save()
        return redirect('detailkomoditas')
    
def delete_detailkomoditas(request, id):
    detailkomoditasobj = models.detail_komoditas.objects.get(id_detailkomoditas=id)
    detailkomoditasobj.delete()
    return redirect('detailkomoditas')

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
    return render(request, 'detailpanen/detailpanen.html', {
        "alldetailpanenobj" : alldetailpanenobj,
    })

@login_required
def create_detailpanen(request):
    if request.method == "GET":
        allpanenobj = models.panen.objects.all()
        allmitraobj = models.mitra.objects.all()
        alldetailkomoditasobj = models.detail_komoditas.objects.all()
        return render(request, 'detailpanen/createdetailpanen.html', {
            'datapanen': allpanenobj,
            'datakomoditas': alldetailkomoditasobj,
            'datamitra': allmitraobj
        })
    elif request.method == "POST":
        id_mitra = request.POST['id_mitra']
        tanggal_panen = request.POST['tanggal_panen']
        id_detailkomoditas = request.POST['id_detailkomoditas']
        jumlahpanen = request.POST["jumlahpanen"]
        tanggalkadaluwarsa = request.POST["tanggalkadaluwarsa"]

        newmitra = models.mitra.objects.get(id_mitra=id_mitra)  # Get the mitra object
        newpanen = models.panen.objects.create(
            id_mitra=newmitra,
            tanggal_panen=tanggal_panen
        )

        newdetailpanen = models.detail_panen.objects.create(
            idpanen=newpanen,
            id_detailkomoditas_id=id_detailkomoditas,
            jumlahpanen=jumlahpanen,
            tanggalkadaluwarsa=tanggalkadaluwarsa
        )

        return redirect('detailpanen')

def update_detailpanen(request, id):
    detailpanenobj = models.detail_panen.objects.get(id_detailpanen=id)
    panenobj = detailpanenobj.idpanen
    allmitraobj = models.mitra.objects.all()
    allpanenobj = models.panen.objects.all()
    alldetailkomoditasobj = models.detail_komoditas.objects.all()

    if request.method == "GET":
        tanggal = detailpanenobj.tanggalkadaluwarsa.strftime('%Y-%m-%d')
        return render(request, 'detailpanen/updatedetailpanen.html', {
            'alldetailpanen': detailpanenobj,
            'datapanen': allpanenobj,
            'datamitra': allmitraobj,
            'datakomoditas': alldetailkomoditasobj,
            'tanggal': tanggal
        })
    elif request.method == "POST":
        id_mitra = request.POST['id_mitra']
        tanggal_panen = request.POST['tanggal_panen']
        id_detailkomoditas = request.POST['id_detailkomoditas']
        jumlahpanen = request.POST["jumlahpanen"]
        tanggalkadaluwarsa = request.POST["tanggalkadaluwarsa"]

        panenobj.id_mitra_id = id_mitra
        panenobj.tanggal_panen = tanggal_panen
        panenobj.save()

        detailpanenobj.id_detailkomoditas_id = id_detailkomoditas
        detailpanenobj.jumlahpanen = jumlahpanen
        detailpanenobj.tanggalkadaluwarsa = tanggalkadaluwarsa
        detailpanenobj.save()

        return redirect('detailpanen')



@login_required
def update_detailpanen(request, id):
    detailpanenobj = models.detail_panen.objects.get(id_detailpanen=id)
    panenobj = detailpanenobj.idpanen
    allmitraobj = models.mitra.objects.all()
    allpanenobj = models.panen.objects.all()
    alldetailkomoditasobj = models.detail_komoditas.objects.all()

    if request.method == "GET":
        tanggal = detailpanenobj.tanggalkadaluwarsa.strftime('%Y-%m-%d')
        return render(request, 'detailpanen/updatedetailpanen.html', {
            'alldetailpanen': detailpanenobj,
            'datapanen': allpanenobj,
            'datamitra' : allmitraobj,
            'datakomoditas': alldetailkomoditasobj,
            'tanggal': tanggal
        })
    elif request.method == "POST":
        id_mitra = request.POST['id_mitra']
        tanggal_panen = request.POST['tanggal_panen']
        id_detailkomoditas = request.POST['id_detailkomoditas']
        jumlahpanen = request.POST["jumlahpanen"]
        tanggalkadaluwarsa = request.POST["tanggalkadaluwarsa"]

        panenobj.id_mitra_id = id_mitra
        panenobj.tanggal_panen = tanggal_panen
        panenobj.save()

        detailpanenobj.id_detailkomoditas_id = id_detailkomoditas
        detailpanenobj.jumlahpanen = jumlahpanen
        detailpanenobj.tanggalkadaluwarsa = tanggalkadaluwarsa
        detailpanenobj.save()

        return redirect('detailpanen')


@login_required
def delete_detailpanen(request,id):
    detailpanenobj = models.detail_panen.objects.get(id_detailpanen=id)
    detailpanenobj.delete()
    return redirect('detailpanen')


@login_required
def detail_jual(request):
    alldetailjualobj = models.detail_jual.objects.all()
    return render(request, 'detailjual/detailjual.html', {
        "alldetailjualobj" : alldetailjualobj,
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
            id_penjualan_id = id_penjualan,
            id_produk_id = id_produk,
            jumlah = jumlah
        )

        return redirect('detailjual')

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


    
