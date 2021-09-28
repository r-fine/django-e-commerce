from django.shortcuts import get_object_or_404, render

from .models import Category, Product, Brand


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def brands(request):
    return {
        'brands': Brand.brands.all()
    }


def all_products(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def brand_list(request, brand_slug=None):
    brand = get_object_or_404(Brand, slug=brand_slug)
    products = Product.objects.filter(brand=brand)
    return render(request, 'store/products/brand.html', {'brand': brand, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    quantity = []
    for q in range(1, product.quantity+1):
        quantity.append(q)
    return render(request, 'store/products/detail.html', {'product': product, 'quantity': quantity})
