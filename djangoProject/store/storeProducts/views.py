from django.shortcuts import render, HttpResponseRedirect

from .models import Product, ProductCategory, Basket
import sys
sys.path.append('/Users/erlankarabaliyev/Desktop/spring kbtu/django/djangoProject/store/users')
from users .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        'title' : 'storeApp',
        # 'products': products,
        'categories' : ProductCategory.objects.all(),
    }

    return render(request, 'storeProducts/index.html', context)


def products(request, category_id=None):
    if category_id:
        category = ProductCategory.objects.get(id = category_id)
        products = Product.objects.filter(category = category)
    else:
        products = Product.objects.all()

    context = {
        'title' : 'storeApp',
        'products' : products,
        'categories' : ProductCategory.objects.all(),
    }
    return render(request, 'storeProducts/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])





