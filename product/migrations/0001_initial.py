# Generated by Django 3.2.18 on 2023-03-08 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, null=True)),
                ('brand_description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True)),
                ('category_description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1000, null=True)),
                ('product_description', models.TextField(null=True)),
                ('product_price', models.FloatField(null=True)),
                ('product_image', models.ImageField(upload_to='product_image')),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.brandmaster')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.categorymaster')),
            ],
        ),
    ]