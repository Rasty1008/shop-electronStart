from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL', db_index=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name



class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL', db_index=True)

    class Meta:
        db_table = 'brand'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['name']

    def __str__(self):
        return self.name


class QuantityOfPoles(models.Model):
    value = models.IntegerField(verbose_name='Количество полюсов', db_index=True)

    class Meta:
        db_table = 'quantity_of_poles'
        verbose_name = 'Количество полюсов'
        verbose_name_plural = 'Количество полюсов'
        ordering = ['value']

    def display_value(self):
        return f"{self.value}P"

    def __str__(self):
        return self.display_value()


class RatedAmperage(models.Model):
    value = models.IntegerField(verbose_name='Номинальный ток', db_index=True)

    class Meta:
        db_table = 'rated_amperage'
        verbose_name = 'Номинальный ток'
        verbose_name_plural = 'Номинальные токи'
        ordering = ['value']

    def display_value(self):
        return f"{self.value}A"

    def __str__(self):
        return self.display_value()


class RatedVoltage(models.Model):
    value = models.IntegerField(verbose_name='Номинальное напряжение', db_index=True)

    class Meta:
        db_table = 'rated_voltage'
        verbose_name = 'Номинальное напряжение'
        verbose_name_plural = 'Номинальные напряжения'
        ordering = ['value']

    def display_value(self):
        return f"{self.value}V"
    
    def __str__(self):
        return self.display_value()

CURRENT_TYPE_CHOICES = [
    ('AC', 'Переменный ток'),
    ('DC', 'Постоянный ток'),
    ('AC/DC', 'Переменный и постоянный ток')
]

class AmperageType(models.Model):
    value = models.CharField(max_length=20,choices=CURRENT_TYPE_CHOICES, verbose_name='Тип тока')

    class Meta:
        db_table = 'amperage_type'
        verbose_name = 'Тип тока'
        verbose_name_plural = 'Типы тока'
        ordering = ['value']

    def __str__(self):
        return self.value



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', db_index=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL', db_index=True)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    article = models.CharField(max_length=100, unique=True, verbose_name='Артикул', db_index=True)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(
        to=Category, 
        null=True, 
        on_delete=models.CASCADE, 
        verbose_name='Категория',
        related_name='products'
        )
    brand = models.ForeignKey(
        to=Brand, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        verbose_name='Бренд',
        related_name='products'
        )
    quantity_of_poles = models.ForeignKey(
        to=QuantityOfPoles, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        verbose_name='Количество полюсов'
        )
    rated_amperage = models.ForeignKey(
        to=RatedAmperage, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        verbose_name='Номинальный ток'
        )
    rated_voltage = models.ForeignKey(
        to=RatedVoltage, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        verbose_name='Номинальное напряжение'
        )
    amperage_type = models.ForeignKey(
        to=AmperageType, 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        verbose_name='Тип тока'
        )

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self):
        return f"{self.name} (Артикул: {self.article})"
    
    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})
    






