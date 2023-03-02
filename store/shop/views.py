from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.

def index(request):
    item = {'product': 'specs', 'price': '12', 'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'}
    data = [item, item, item]

    return render(request, 'shop/index.html',  context={'data': data})
