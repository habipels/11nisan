"""ticari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from anasayfa.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",anasayfa,name="index"),
    path("deneme/",deneme,name="deneme"),
    path("sepet/<int:id>",sepet,name="sepet"),
    path("urun/<str:id>",urun_goster,name="urun"),
    path("kategori/<int:id>",siralama,name="siralama"),
    path("sepetsil/<int:id>",sepet_urun_sil,name="sepet_urun_sil"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("user/",include("user_o.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)