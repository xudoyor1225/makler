from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render,reverse
from django.views.generic import TemplateView,ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import UyRasmlari, Uylar, Xususiyati, Vazifalar,Review

from django.shortcuts import render, redirect
from .forms import MijozForm, UylarForm, XususiyatForm, UypictureForm, UserLoginForm, UserRegistrForm,ReviewForm


class Home_sahifasi(View):
    def get(self, request):
        xususiyatlar = Xususiyati.objects.all()
        vazifa = Vazifalar.objects.all()


        return render(request, "home.html", {"xususiyatlar":xususiyatlar, "vaz":vazifa})


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
        form=XususiyatForm(data=request.POST,files=request.FILES)
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
        form=UylarForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('xususiyat')
        else:
            return render(request,"uylar.html",{"form":form})




class detail_home(View):
    def get(self, request, a):
        review_form = ReviewForm()
        uy = Xususiyati.objects.get(id=a).uy
        # print(uy)
        sharxlar = Review.objects.filter(uy_id=uy.id)
        xususiyat = Xususiyati.objects.get(pk=a)
        Uy_picture = UyRasmlari.objects.filter(xususiyat_id=a)
        return render(request, 'detail_img.html', {'Uy_picture':Uy_picture, "xususiyat":xususiyat,'form': review_form,'sharxlar': sharxlar})

    def post(self, request, a):
        review_form = ReviewForm(data=request.POST)
        uy = Xususiyati.objects.get(id=a).uy
        # print(uy)
        sharxlar = Review.objects.filter(uy_id=uy.id)
        # print(sharxlar)
        if review_form.is_valid():
            Review.objects.create(
                uy_id=uy,
                user_id=request.user,
                description=review_form.cleaned_data['description'],
                stars=review_form.cleaned_data["stars"]
            )
            return redirect(reverse("detail_home", kwargs={'a': uy.id}))
        print(sharxlar)
        return render(request, "detail_img.html", {'uy': uy, 'sharxlar': sharxlar, 'form': review_form})

class addpicture(View):
    def get(self,request):
        form=UypictureForm()
        return render(request,"addpicturre.html",{"form":form})
    def post(self,request):
        form=UypictureForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addpicture')
        else:
            return render(request,"addpicturre.html",{"form":form})


class LoginView(View):
    def get(self, request):
        user = UserLoginForm()
        return render(request, "login.html", {'user':user})

    def post(self, request):
        check = AuthenticationForm(data=request.POST)

        if check.is_valid():
            user = check.get_user()
            login(request, user)
            messages.success(request, "Siz tizimga kirdingiz!")
            return redirect('home')
        else:
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz tizimdan chiqdingiz!")
        return redirect("home")


class HomesView(View):
    def get(self, request,id):
        uylar = Xususiyati.objects.filter(vazifasi=id)
        xususiyatlar = Xususiyati.objects.all()
        vazifa = Vazifalar.objects.all()

        search_query = request.GET.get('q','')
        if search_query:
            uylar = Xususiyati.objects.filter(uy__joylashuvi__icontains=search_query)




        return render(request, "home.html", {"xususiyatlar": xususiyatlar, "vaz": vazifa,"uylar":uylar,"search":search_query})

class UserRegistrView(View):
    def get(self,request):
        form=UserRegistrForm()
        return render(request,'register.html',{'form':form})

    def post(self, request):
        form = UserRegistrForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "register.html", {'form': form})