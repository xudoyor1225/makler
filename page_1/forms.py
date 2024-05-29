# forms.py
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from .models import Mijoz, Uylar, Xususiyati, UyRasmlari,Review
from django.contrib.auth.models import User
class MijozForm(forms.ModelForm):
    class Meta:
        model = Mijoz
        fields = '__all__'

class UylarForm(forms.ModelForm):
    class Meta:
        model = Uylar
        fields = '__all__'

class XususiyatForm(forms.ModelForm):
    class Meta:
        model = Xususiyati
        fields = '__all__'

class UypictureForm(forms.ModelForm):
    class Meta:
        model = UyRasmlari
        fields = ['xususiyat_id','picture']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)

class UserRegistrForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def save(self):
        super().save()
        user = User.objects.get(username=self.cleaned_data['username'])
        user.set_password(self.cleaned_data['password'])
        user.save()

class ReviewForm(forms.ModelForm):
    stars = forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Review
        fields = ['description','stars']