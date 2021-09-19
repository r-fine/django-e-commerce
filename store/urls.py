from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('categories/<slug:category_slug>/',
         views.category_list, name='category_list'),
    path('brands/<slug:brand_slug>/',
         views.brand_list, name='brand_list'),
]
