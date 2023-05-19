from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
# Create your views here.

def produk(request):
     allprodukobj = models.produk.objects.all()

     return render (request, 'obat.html',{
    'allprodukobj' : allprodukobj,  
    })

pass
