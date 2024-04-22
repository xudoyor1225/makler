from django.urls import path
from .views import Home_sahifasi, mijozqoshish, buildhous, xususiyat, uylar

urlpatterns = [
    path('', Home_sahifasi.as_view(), name='home'),
    path('mijoz/', mijozqoshish.as_view(), name='mijoz'),
    path('buildhous/', buildhous.as_view(), name='buildhous'),
    path('xususiyat/', xususiyat.as_view(), name='xususiyat'),
    path('uy/', uylar.as_view(), name='uylar'),

]