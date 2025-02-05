from django.contrib import admin

from goods.models import Categories, Brands, Products, Quantity_of_poles, Rated_amperage, Rated_voltage, Amperage_type

#admin.site.register(Catigories)
#admin.site.register(Brands)
#admin.site.register(Products)

@admin.register(Categories)
class CatigoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Quantity_of_poles)
class Quantity_of_polesAdmin(admin.ModelAdmin):
    list_display = ['value',]

@admin.register(Rated_amperage)
class Rated_amperageAdmin(admin.ModelAdmin):
    list_display = ['value',]

@admin.register(Rated_voltage)
class Rated_voltageAdmin(admin.ModelAdmin):
    list_display = ['value',]

@admin.register(Amperage_type)
class Amperage_typeAdmin(admin.ModelAdmin):
    list_display = ['value',]