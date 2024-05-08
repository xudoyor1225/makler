# forms.py
from django import forms
from .models import Mijoz, Uylar, Xususiyati

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