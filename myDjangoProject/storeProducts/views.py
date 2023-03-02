from django.shortcuts import render

from storeProducts.models import ProductCategory, Product


def products(request, category_id=None):
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    context = {
        'title': 'storeApp',
        'products': products,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'storeProducts/products.html', context)
