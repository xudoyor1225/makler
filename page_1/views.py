from django.shortcuts import render
from django.views.generic import TemplateView,ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UyRasmlari, Uylar, Xususiyati, Vazifalar

from django.shortcuts import render, redirect
from .forms import MijozForm, UylarForm,XususiyatForm

class Home_sahifasi(View):
    def get(self, request):
        xususiyatlar = Xususiyati.objects.all()
        search = Uylar.objects.all().order_by('joylashuvi')
        search_query = request.GET.get('q', '')
        if search_query:
            search = Uylar.objects.filter(title__icontains=search_query)

        return render(request, "home.html", {"xususiyatlar":xususiyatlar, "search":search_query})

class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class mijozqoshish(View):
    def get(self,request):
        form=MijozForm()
        return render(request,"mijozqoshish.html",{"form":form})
    def post(self,request):
        form=MijozForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('uylar')
        else:
            return render(request,"mijozqoshish.html",{"form":form})



class xususiyat(View):
    def get(self,request):
        form=XususiyatForm()
        return render(request,"xususiyatlari.html",{"form":form})
    def post(self,request):
        form=XususiyatForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,"xususiyatlari.html",{"form":form})


class uylar(View):
    def get(self,request):
        form=UylarForm()
        return render(request,"uylar.html",{"form":form})
    def post(self,request):
        form=UylarForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('xususiyat')
        else:
            return render(request,"uylar.html",{"form":form})




class detail_home(View):
    def get(self, request, a):
        xususiyat = Xususiyati.objects.get(pk=a)
        Uy_picture = UyRasmlari.objects.filter(xususiyat_id=a)

        return render(request, 'detail_img.html', {'Uy_picture':Uy_picture, "xususiyat":xususiyat})

