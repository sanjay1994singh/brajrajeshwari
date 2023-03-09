from django.urls import path
from.import views
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('product-details/<int:id>/',views.product_details,name='product_details'),
]