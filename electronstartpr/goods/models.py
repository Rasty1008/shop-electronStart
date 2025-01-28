from django.db import models

class Catigories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class Brands(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'brand'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name




class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    article = models.CharField(max_length=100, unique=True, verbose_name='Артикул')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    category_id = models.ForeignKey(to=Catigories, on_delete=models.CASCADE, verbose_name='Категория')
    brand_id = models.ForeignKey(to=Brands, on_delete=models.CASCADE, verbose_name='Бренд')
    

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)

    def __str__(self):
        return self.name



class Specifications(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        db_table = 'specispecification'
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.name




class ProductSpecifications(models.Model):
    product_id = models.ForeignKey(to=Products, on_delete=models.PROTECT, verbose_name='Товар')
    specification_id = models.ForeignKey(to=Specifications, on_delete=models.PROTECT, verbose_name='Характеристика')
    value = models.CharField(max_length=20, unique=False, blank=True, null=True, verbose_name='Значение')

    class Meta:
        db_table = 'product_specification'
        verbose_name = 'Характеристику товара'
        verbose_name_plural = 'Характеристики товаров'

    def __str__(self):
        return self.value
