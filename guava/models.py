from django.db import models

# Create your models here.
class mitra(models.Model):
    id_mitra = models.AutoField(primary_key=True)
    nama_mitra = models.CharField(max_length=30)
    alamat_mitra = models.TextField(blank=True, null=True)
    nomor_mitra = models.PositiveIntegerField()
    tanggal_mulai_mitra = models.DateField()
    durasi_kontrak = models.PositiveIntegerField()
    luas_lahan = models.PositiveIntegerField()

    def __str__(self):
        return str(self.nama_mitra)
    
class pembeli(models.Model):
    id_pembeli = models.AutoField(primary_key=True)
    nama_pembeli = models.CharField(max_length=30)
    nomor_pembeli = models.PositiveIntegerField()
    alamat_pembeli = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.nama_pembeli)


class penjualan(models.Model):
    id_penjualan = models.AutoField(primary_key=True)
    idpembeli = models.ForeignKey(pembeli, on_delete=models.CASCADE)
    tanggalpenjualan = models.DateField()

    def _str_(self):
        return str(self.idpembeli)

class produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    namaproduk = models.CharField(max_length=15)
    satuanproduk = models.CharField(max_length=15)
    hargaproduk = models.IntegerField()

    def __str__(self):
        return str(self.namaproduk)    


class detail_jual(models.Model):
    id_detailjual = models.AutoField(primary_key=True)
    id_penjualan = models.ForeignKey(penjualan, on_delete=models.CASCADE)
    id_produk = models.ForeignKey(produk, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id_produk)   

class komoditas(models.Model):
    id_komoditas = models.AutoField(primary_key=True)
    nama_komoditas = models.CharField(max_legth=50)
    satuan = models.IntegerField()
    kode_grade = models.CharField(max_legth=50)
    harga_sewa = models.IntegerField()

    def _str_(self):
        return str(self.nama_komoditas) 

class panen(models.Model):
    id_panen = models.AutoField(primary_key=True)
    id_mitra = models.ForeignKey(mitra, on_delete=models.CASCADE)
    biaya_pembelian = models.IntegerField()
    tanggal_panen = models.DateField()

    def _str_(self):
        return str(self.id_panen)

class transaksi_lain(models.Model):
    id_transaksi = models.AutoField(primary_key=True)
    jenis_transaksi = models.CharField(max_length=50)
    tanggal_transaksi = models.DateField()
    biaya = models.IntegerField()

    def _str_(self):
        return str(self.id_transaksi)
    
class detail_panen(models.Model):
    id_detailpanen = models.AutoField(primary_key=True)
    idpanen = models.ForeignKey(panen, on_delete=models.CASCADE)
    idkomoditas= models.ForeignKey(komoditas, on_delete=models.CASCADE)
    jumlahpanen = models.IntegerField()
    tanggalkadaluwarsa = models.DateField()

    def __str__(self):
        return str(self.idpanen)
