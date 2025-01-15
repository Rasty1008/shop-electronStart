from django.contrib import admin

from goods.models import Catigories, Brands, Products, Specifications, ProductSpecifications

#admin.site.register(Catigories)
#admin.site.register(Brands)
#admin.site.register(Products)
#admin.site.register(Specifications)
#admin.site.register(ProductSpecifications)

@admin.register(Catigories)
class CatigoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Specifications)
class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(ProductSpecifications)
class ProductSpecificationsAdmin(admin.ModelAdmin):
    list_display = ['value',]