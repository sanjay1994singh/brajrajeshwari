from django.shortcuts import render

from product.models import BrandMaster, CategoryMaster, ProductMaster

# Create your views here.
def home_page(request):
    b_data = BrandMaster.objects.all()
    p_data = ProductMaster.objects.all()
    c_data = CategoryMaster.objects.all()

    context = {
        'b_data':b_data,
        'p_data':p_data,
        'c_data':c_data,     
    }
    return render(request,'index.html',context)

def product_details(request,id):
    b_data = BrandMaster.objects.all()
    p_data = ProductMaster.objects.get(id=id)
    c_data = CategoryMaster.objects.all()

    context = {
        'b_data':b_data,
        'p_data':p_data,
        'c_data':c_data,     
    }
    return render(request,'product_details.html',context)
