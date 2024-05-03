from django.shortcuts import render
from django.views.generic import TemplateView,ListView, View
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import UyRasmlari, Uylar, Xususiyati, Vazifalar


# Create your views here.

class Home_sahifasi(View):
    def get(self, request):
        xususiyatlar = Xususiyati.objects.all()
        search = Uylar.objects.all().order_by('joylashuvi')
        search_query = request.GET.get('q', '')
        if search_query:
            search = Uylar.objects.filter(title__icontains=search_query)

        return render(request, "home.html", {"xususiyatlar":xususiyatlar, "search":search_query})



class mijozqoshish(TemplateView):
    template_name = 'mijozqoshish.html'

class xususiyat(TemplateView):
    template_name = 'xususiyatlari.html'

class uylar(TemplateView):
    template_name = 'uylar.html'

class detail_home(View):
    def get(self, request, a):
        xususiyat = Xususiyati.objects.get(pk=a)
        Uy_picture = UyRasmlari.objects.filter(xususiyat_id=a)

        return render(request, 'detail_img.html', {'Uy_picture':Uy_picture, "xususiyat":xususiyat})

