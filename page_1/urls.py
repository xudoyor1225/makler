from django.urls import path
from .views import Home_sahifasi, mijozqoshish, xususiyat, uylar, detail_home, addpicture, LoginView, LogoutView,HomesView,UserRegistrView

urlpatterns = [
    path('', Home_sahifasi.as_view(), name='home'),
    path('mijoz/', mijozqoshish.as_view(), name='mijoz'),

    path('xususiyat/', xususiyat.as_view(), name='xususiyat'),
    path('uy/', uylar.as_view(), name='uylar'),
    path('detail/<a>/', detail_home.as_view(), name='detail_home'),
    path('addpicture/', addpicture.as_view(), name='addpicture'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('uylar/<id>/',HomesView.as_view(),name="homes"),
    # path('delete/<b>/', CommentDetailViev.as_view(), name='delete')
    path('register/',UserRegistrView.as_view(),name='register'),


]