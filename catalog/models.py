from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE,verbose_name='категория')
    purchase_price = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='цена за штуку')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)



    def __str__(self):
        return f'{self.name} ({self.product_category}'



    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ('name',)

