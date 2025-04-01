from django.contrib import admin

from goods.models import Category, Brand, Product, QuantityOfPoles, RatedAmperage, RatedVoltage, AmperageType

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(QuantityOfPoles)
class QuantityOfPolesAdmin(admin.ModelAdmin):
    list_display = ['value',]

@admin.register(RatedAmperage)
class RatedAmperageAdmin(admin.ModelAdmin):
    list_display = ['value',]

@admin.register(RatedVoltage)
class RatedVoltageAdmin(admin.ModelAdmin):
    list_display = ['value',]

@admin.register(AmperageType)
class AmperageTypeAdmin(admin.ModelAdmin):
    list_display = ['value',]