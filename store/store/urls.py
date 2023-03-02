from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('storeProduct', include('storeProduct.urls')),
    path('shop', include('shop.urls'))
]
