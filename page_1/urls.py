from django.urls import path
from .views import Home_sahifasi, mijozqoshish, xususiyat, uylar,detail_home

urlpatterns = [
    path('', Home_sahifasi.as_view(), name='home'),
    path('mijoz/', mijozqoshish.as_view(), name='mijoz'),

    path('xususiyat/', xususiyat.as_view(), name='xususiyat'),
    path('uy/', uylar.as_view(), name='uylar'),
    path('deatil/<a>/', detail_home.as_view(), name='detail_home'),


]