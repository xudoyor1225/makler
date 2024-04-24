from django.shortcuts import render
from django.views.generic import TemplateView,ListView, View
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import UyRasmlari, Uylar, Xususiyati, Vazifalar


# Create your views here.

class Home_sahifasi(View):
    def get(self, request):
        vazifa = Vazifalar.objects.get(pk=1)
        xususiyatlar = vazifa.xususiyati_set.all()

        xususiyat_photos = []
        for xususiyat in xususiyatlar:
            photo = xususiyat.uyrasmlari_set.all()[0]
            xususiyat_photos.append([photo, xususiyat])








        # uylar = UyRasmlari.objects.all().order_by('id')
        # uylar_id = Uylar.objects.values_list('id',flat=True)


        # search_query = request.GET.get('q', '')
        # if search_query:
        #     kitoblar = UyRasmlari.objects.filter(title__icontains=search_query)
        #
        # paginator = Paginator(uylar, 6)
        #
        # page_num = request.GET.get('bet', 1)
        #
        # page = paginator.page(page_num)
        #
        return render(request, "home.html", {'xususiyat_photos': xususiyat_photos})
        #


class mijozqoshish(TemplateView):
    template_name = 'mijozqoshish.html'
class buildhous(View):
    def get(self, request):
        kitoblar = UyRasmlari.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            kitoblar = UyRasmlari.objects.filter(title__icontains=search_query)

        paginator = Paginator(kitoblar, 6)

        page_num = request.GET.get('bet', 1)

        page = paginator.page(page_num)

        return render(request, "buildhous.html", {'page':page, 'search':search_query})

class xususiyat(TemplateView):
    template_name = 'xususiyatlari.html'

class uylar(TemplateView):
    template_name = 'uylar.html'