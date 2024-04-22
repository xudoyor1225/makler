from django.contrib import admin

# Register your models here.
from .models import Mijoz, Uylar, Vazifalar, Xususiyati, Stars, UyRasmlari


admin.site.register(Mijoz)
admin.site.register(Uylar)
admin.site.register(Vazifalar)
admin.site.register(Xususiyati)
admin.site.register(Stars)
admin.site.register(UyRasmlari)
