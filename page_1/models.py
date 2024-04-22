# Create your models here.
from django.db import models
class Mijoz(models.Model):
    ismi = models.CharField(max_length=255)
    familyasi = models.CharField(max_length=255)
    t_sana = models.DateField()
    tel = models.CharField(max_length=20)
    yashash_manzili = models.TextField()

    def __str__(self):
        return str(self.ismi)

class Uylar(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    holati = models.TextField()
    yashash_maydoni = models.CharField(max_length=255)
    xonalar_soni = models.BigIntegerField()
    joylashuvi = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Stars(models.Model):
    id = models.BigAutoField(primary_key=True)
    stars = models.BigIntegerField()

    def __str__(self):
        return str(self.stars)

class UyRasmlari(models.Model):
    id = models.BigAutoField(primary_key=True)
    uy = models.ForeignKey(Uylar, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg')

    def __str__(self):
        return f"{str(self.id), str(self.uy)}"


class Vazifalar(models.Model):
    vazifa = models.CharField(max_length=50)

    def __str__(self):
        return f"{str(self.id),str(self.vazifa)}"

class Xususiyati(models.Model):
    xususiyat_id = models.ForeignKey(Uylar, on_delete=models.CASCADE)
    vazifasi = models.ForeignKey(Vazifalar, on_delete=models.CASCADE)
    narxi = models.CharField(max_length=255)
    sana = models.DateTimeField()
    star = models.ForeignKey(Stars, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uy)

