from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')

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


class Quantity_of_poles(models.Model):
    value = models.CharField(max_length=20, verbose_name='Количество полюсов')

    class Meta:
        db_table = 'quantity_of_poles'
        verbose_name = 'Количество полюсов'

    def __str__(self):
        return self.value


class Rated_amperage(models.Model):
    value = models.CharField(max_length=20, verbose_name='Номинальный ток')

    class Meta:
        db_table = 'rated_amperage'
        verbose_name = 'Номинальный ток'

    def __str__(self):
        return self.value


class Rated_voltage(models.Model):
    value = models.CharField(max_length=20, verbose_name='Номинальное напряжение')

    class Meta:
        db_table = 'rated_voltage'
        verbose_name = 'Номинальное напряжение'

    def __str__(self):
        return self.value


class Amperage_type(models.Model):
    value = models.CharField(max_length=20, verbose_name='Тип тока')

    class Meta:
        db_table = 'amperage_type'
        verbose_name = 'Тип тока'

    def __str__(self):
        return self.value



class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    article = models.CharField(max_length=100, unique=True, verbose_name='Артикул')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    category_id = models.ForeignKey(to=Categories, null=True, on_delete=models.CASCADE, verbose_name='Категория')
    brand_id = models.ForeignKey(to=Brands, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Бренд')
    quantity_of_poles_id = models.ForeignKey(to=Quantity_of_poles, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Количество полюсов')
    rated_amperage_id = models.ForeignKey(to=Rated_amperage, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Номинальный ток')
    rated_voltage_id = models.ForeignKey(to=Rated_voltage, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Номинальное напряжение')
    amperage_type_id = models.ForeignKey(to=Amperage_type, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Тип тока')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id',)

    def __str__(self):
        return self.name






