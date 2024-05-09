# forms.py
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from .models import Mijoz, Uylar, Xususiyati, UyRasmlari
from django.contrib.auth.models import User
class MijozForm(forms.ModelForm):
    class Meta:
        model = Mijoz
        fields = ['ismi', 'familyasi', 't_sana', 'tel', 'yashash_manzili']

class UylarForm(forms.ModelForm):
    class Meta:
        model = Uylar
        fields = ['mijoz', 'holati', 'yashash_maydoni','xonalar_soni', 'joylashuvi']

class XususiyatForm(forms.ModelForm):
    class Meta:
        model = Xususiyati
        fields = '__all__'

class UypictureForm(forms.ModelForm):
    class Meta:
        model = UyRasmlari
        fields = ['xususiyat_id','picture']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
