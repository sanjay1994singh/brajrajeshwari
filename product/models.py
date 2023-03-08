from django.db import models

# Create your models here.
class BrandMaster(models.Model):
    brand_name = models.CharField(max_length=100,null=True)
    brand_description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.brand_name

class CategoryMaster(models.Model):
    category_name = models.CharField(max_length=100,null=True)
    category_description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.category_name

class ProductMaster(models.Model):
    product_brand = models.ForeignKey(BrandMaster,models.PROTECT)
    product_category = models.ForeignKey(CategoryMaster,models.PROTECT)
    product_name = models.CharField(max_length=1000,null=True)
    product_description = models.TextField(null=True)
    product_price = models.FloatField(null=True)
    product_image = models.ImageField(upload_to='product_image')
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.product_name