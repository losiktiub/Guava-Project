from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.mitra)
admin.site.register(models.pembeli)
admin.site.register(models.penjualan)
admin.site.register(models.produk)
admin.site.register(models.detail_jual)
admin.site.register(models.komoditas)
admin.site.register(models.panen)
admin.site.register(models.transaksi_lain)
admin.site.register(models.detail_panen)