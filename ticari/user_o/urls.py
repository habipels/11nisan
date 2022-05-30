

from django.urls import path,include
from .views import *
app_name = "users"
urlpatterns = [
   path("login/",giris,name="login"),
   path("logout/",cikis,name="logout"),
   path("register/",kayit,name="register"),
   
]