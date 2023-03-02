from django.urls import path

from . import views

app_name = 'storeProducts'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/category/<int:category_id>/', views.products, name='category'),
]
