from django.contrib import admin
from . models import BrandMaster,CategoryMaster,ProductMaster


class BrandMasterAdmin(admin.ModelAdmin):
    list_display = ['brand_name','created_at']

class CategoryMasterAdmin(admin.ModelAdmin):
    list_display = ['category_name','created_at']

class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_price','product_brand']

admin.site.register(BrandMaster,BrandMasterAdmin)
admin.site.register(CategoryMaster,CategoryMasterAdmin)
admin.site.register(ProductMaster,ProductMasterAdmin)
