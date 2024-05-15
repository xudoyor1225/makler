# forms.py
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from .models import Mijoz, Uylar, Xususiyati, UyRasmlari
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
