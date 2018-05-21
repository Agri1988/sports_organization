from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=1024, blank=False, null=False, verbose_name="Наименование услуги")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Category (models.Model):
    name = models.CharField(max_length=256, blank=False, null=False, verbose_name="Наименование категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# class Subscription (models.Model):
#     client = models.ForeignKey()
