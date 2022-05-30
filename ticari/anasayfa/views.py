from os import sep
from django.shortcuts import redirect, render,HttpResponse
from .models import *
# Create your views here.
def anasayfa(request):
    kategoriler = kategori.objects.all()
    urunler = urun.objects.all()
    sozluk = {"kategoriler":kategoriler,"urunler":urunler}
    return render(request,"anasayfa_temp/index.html",sozluk)
def deneme(request):
    return render(request,"anasayfa_temp/deneme.html")

def urun_goster(request,id):
    urunler = urun.objects.filter(isim = id)
    print(urunler)
    for i in urunler:
        m = i.kategorisi_id
    benzer = urun.objects.filter(kategorisi_id = m)[:3]
    sozluk = {"urunler":urunler,"benzer":benzer}
    
    return render(request,"anasayfa_temp/urun_sayfa.html",sozluk)

def siralama(request,id):
    card = 0
    liste = []
    if  request.user.is_authenticated:
        card = sepetler.objects.filter(user =  request.user)
        for i in card:
            liste.append(i.urunler_id)
    urunler = urun.objects.filter(kategorisi_id = id)
    if request.GET:
        fiyat = int(request.GET.get("fiyat"))+1
        urunler = urun.objects.filter(kategorisi_id = id, urun_fiyat__lt = fiyat )
    sozluk = {"urunler":urunler,"liste":liste}
    return render(request,"anasayfa_temp/siralama.html",sozluk)

def sepet(request,id):
    print(id)
    urunler = urun.objects.filter(id = id)
    kategori_idi=0
    for i in urunler:
        kategori_idi = i.kategorisi_id
    print("selam")
    sepetler.objects.create(user = request.user,urunler_id = id)
    return redirect("/kategori/"+str(kategori_idi))

def sepet_urun_sil(request,id):
    sepetler.objects.filter(user = request.user,urunler_id =id).delete()
    urunler = urun.objects.filter(id = id)
    kategori_idi=0
    for i in urunler:
        kategori_idi = i.kategorisi_id
    return redirect("/kategori/"+str(kategori_idi))