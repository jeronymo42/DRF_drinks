from django.db import models

# Create your models here.

class BeverageType(models.Model):
    name = models.CharField("Категория", max_length=50)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Drinks(models.Model):
    name = models.CharField("Название", max_length=150)
    degree = models.PositiveIntegerField("Градус", default=0,)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="drinks/", blank=True)
    beverage_type = models.ForeignKey(BeverageType,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Напиток"
        verbose_name_plural = "Напитки"

