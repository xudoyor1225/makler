from django.contrib import admin

# Register your models here.
from .models import Mijoz, Uylar, Vazifalar, Xususiyati, Stars, UyRasmlari,Review


class Mijoz_admin(admin.ModelAdmin):
    search_fields=['ismi','familyasi','t_sana','tel','yashash_manzili']
    list_display=['ismi','familyasi','t_sana','tel','yashash_manzili']
class Stars_admin(admin.ModelAdmin):
    search_fields=['stars']
    list_display=['stars']
class Uylar_admin(admin.ModelAdmin):
    search_fields=['holati','yashash_maydoni','xonalar_soni','joylashuvi']
    list_display=['mijoz_id','holati','yashash_maydoni','xonalar_soni','joylashuvi']

class Vazifalar_admin(admin.ModelAdmin):
    search_fields=['vazifa']
    list_display=['vazifa']

class Xususiyati_admin(admin.ModelAdmin):
    search_fields=['narxi','sana','defaultimage']
    list_display=['uy','vazifasi','narxi','sana','star','defaultimage']
class UyRasm_admin(admin.ModelAdmin):
    search_fields=['picture']
    list_display=['xususiyat_id','picture']
class Review_admin(admin.ModelAdmin):
    search_fields=['description','stars']
    list_display=['uy_id','description','stars','user_id']
admin.site.register(Mijoz,Mijoz_admin)
admin.site.register(Uylar,Uylar_admin)
admin.site.register(Vazifalar,Vazifalar_admin)
admin.site.register(Xususiyati,Xususiyati_admin)
admin.site.register(Stars,Stars_admin)
admin.site.register(UyRasmlari,UyRasm_admin)
admin.site.register(Review,Review_admin)