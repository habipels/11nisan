from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class kategori(models.Model):
    isim = models.CharField(max_length= 100)
    def __str__(self) :
        return self.isim
class urun(models.Model):
    isim = models.CharField(max_length=100)
    urun_gorseli = models.FileField(upload_to='urunresim/',blank = True,null = True,verbose_name="Ürün Resimleri")
    kategorisi = models.ForeignKey(kategori,on_delete=models.CASCADE)
    urun_fiyat = models.BigIntegerField()
    uretim_yili = models.BigIntegerField()
    urun_aciklama = RichTextField(null = True)
    def __str__(self) :
        return self.isim

class sepetler(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    urunler = models.ForeignKey(urun, on_delete=models.CASCADE)